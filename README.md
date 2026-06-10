# 🤖 FAQ Chatbot — NLP Project
Built with Python (custom TF-IDF NLP engine) + Flask + HTML/CSS/JS

## 📁 Project Structure
```
faq_chatbot/
├── app.py              # Flask web server
├── chatbot_engine.py   # NLP engine (tokenizer + TF-IDF classifier)
├── intents.json        # FAQ intents, patterns & responses
├── requirements.txt    # Dependencies
├── templates/
│   └── index.html      # Chat UI
└── README.md
```

## ⚙️ How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Start the server
```bash
python app.py
```

### 3. Open in browser
```
http://localhost:5000
```

---

## 🧠 How the NLP Works

1. **Tokenization** — splits user input into tokens, removes stop words
2. **Stemming** — reduces words to root form (e.g. "pricing" → "price")
3. **TF-IDF Vectorization** — converts tokens to weighted vectors
4. **Cosine Similarity** — compares query vector to each intent's patterns
5. **Keyword Boost** — gives extra score for multi-word exact matches
6. **Response Selection** — picks a random response from matched intent

> No external NLP libraries needed — pure Python math!

---

## ➕ How to Add New FAQs

Open `intents.json` and add a new intent block:

```json
{
  "tag": "shipping",
  "patterns": [
    "how long does shipping take",
    "delivery time",
    "when will my order arrive"
  ],
  "responses": [
    "Standard shipping takes 5–7 business days.",
    "We deliver within 5–7 working days across India."
  ]
}
```

Restart the server and it works instantly — no retraining needed!

---

## 🚀 Possible Upgrades (for your resume!)
- Add NLTK for better stemming (`PorterStemmer`)
- Integrate Hugging Face for semantic similarity
- Add a database to log conversations
- Deploy on Heroku / Render for a live URL
- Add multi-turn memory (conversation history)
