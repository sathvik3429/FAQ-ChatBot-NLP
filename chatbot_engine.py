"""
chatbot_engine.py
NLP engine for FAQ chatbot - Tokenizer and Stemmer
"""
import re

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

if __name__ == "__main__":
    test = "What are your opening hours on weekdays?"
    print("Input   :", test)
    print("Tokens  :", tokenize(test))
    print("Stemmed :", normalize(test))
