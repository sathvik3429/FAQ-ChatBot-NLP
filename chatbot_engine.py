"""
chatbot_engine.py
NLP engine for FAQ chatbot - Tokenizer, Stemmer, and TF-IDF Classifier
"""
import re
import json
import math
import random

STOP_WORDS = {"i", "me", "my", "we", "our", "you", "your", "he", "she", "it",
              "is", "are", "was", "were", "be", "been", "being", "have", "has",
              "do", "does", "did", "a", "an", "the", "and", "or", "but", "in",
              "on", "at", "to", "for", "of", "with", "about", "can", "could",
              "would", "will", "should", "may", "might", "what", "how", "when",
              "where", "which", "who", "that", "this", "these", "those"}

def tokenize(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    tokens = text.split()
    return [t for t in tokens if t not in STOP_WORDS and len(t) > 1]

def stem(word):
    suffixes = ["ing", "tion", "ness", "ment", "able", "ible", "ed", "er", "ly", "es", "s"]
    for suffix in suffixes:
        if word.endswith(suffix) and len(word) - len(suffix) >= 3:
            return word[:-len(suffix)]
    return word

def normalize(text):
    return [stem(t) for t in tokenize(text)]

class IntentClassifier:
    def __init__(self, intents_path):
        with open(intents_path, 'r', encoding='utf-8') as f:
            self.intents = json.load(f)['intents']
        
        # Build vocabulary and document frequency
        self.vocab = set()
        self.doc_freq = {}
        self.intent_vectors = []
        
        for intent in self.intents:
            # Combine all patterns for this intent
            all_tokens = []
            for pattern in intent['patterns']:
                tokens = normalize(pattern)
                all_tokens.extend(tokens)
                self.vocab.update(tokens)
            
            # Calculate TF for this intent
            tf = {}
            for token in all_tokens:
                tf[token] = tf.get(token, 0) + 1
            
            # Store TF and tokens for this intent
            self.intent_vectors.append({
                'tag': intent['tag'],
                'tokens': all_tokens,
                'tf': tf,
                'responses': intent['responses']
            })
        
        # Calculate IDF for all tokens
        total_docs = len(self.intents)
        for token in self.vocab:
            doc_count = sum(1 for iv in self.intent_vectors if token in iv['tf'])
            self.doc_freq[token] = math.log(total_docs / (doc_count + 1))
    
    def _get_tfidf_vector(self, tokens):
        vector = {}
        for token in tokens:
            if token in self.vocab:
                tf = tokens.count(token)
                idf = self.doc_freq.get(token, 0)
                vector[token] = tf * idf
        return vector
    
    def _cosine_similarity(self, vec1, vec2):
        dot_product = sum(vec1.get(t, 0) * vec2.get(t, 0) for t in set(vec1) | set(vec2))
        norm1 = math.sqrt(sum(v**2 for v in vec1.values()))
        norm2 = math.sqrt(sum(v**2 for v in vec2.values()))
        if norm1 == 0 or norm2 == 0:
            return 0
        return dot_product / (norm1 * norm2)
    
    def _keyword_boost(self, query_tokens, intent_tokens):
        """Boost score for multi-word exact matches"""
        query_str = ' '.join(query_tokens)
        intent_str = ' '.join(intent_tokens)
        boost = 0
        for i in range(2, min(4, len(query_tokens) + 1)):
            for j in range(len(query_tokens) - i + 1):
                phrase = ' '.join(query_tokens[j:j+i])
                if phrase in intent_str:
                    boost += i * 0.1
        return boost
    
    def chat(self, user_input):
        query_tokens = normalize(user_input)
        if not query_tokens:
            return {"response": "I didn't understand that. Could you rephrase?", "tag": "unknown"}
        
        query_vector = self._get_tfidf_vector(query_tokens)
        
        best_match = None
        best_score = 0
        
        for intent_vec in self.intent_vectors:
            intent_vector = self._get_tfidf_vector(intent_vec['tokens'])
            similarity = self._cosine_similarity(query_vector, intent_vector)
            boost = self._keyword_boost(query_tokens, intent_vec['tokens'])
            total_score = similarity + boost
            
            if total_score > best_score:
                best_score = total_score
                best_match = intent_vec
        
        if best_match and best_score > 0.1:
            response = random.choice(best_match['responses'])
            return {"response": response, "tag": best_match['tag']}
        else:
            return {"response": "I'm not sure I understand. Could you ask differently?", "tag": "unknown"}

if __name__ == "__main__":
    test = "What are your opening hours on weekdays?"
    print("Input   :", test)
    print("Tokens  :", tokenize(test))
    print("Stemmed :", normalize(test))
