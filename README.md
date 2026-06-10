# 🤖 FAQ Chatbot — NLP Project

> An NLP-powered FAQ assistant built from scratch — no ML libraries required

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square)
![Flask](https://img.shields.io/badge/Flask-3.0-green?style=flat-square)
![NLP](https://img.shields.io/badge/NLP-TF--IDF-purple?style=flat-square)
![Deployed](https://img.shields.io/badge/Deployed-Vercel-black?style=flat-square)

🌐 **Live Demo:** https://faq-chat-bot-kk5h6ofdd-rudrarapusathvik-2637s-projects.vercel.app

---

## 📌 About

A rule-based FAQ chatbot powered by a custom NLP engine built entirely in pure Python — no NLTK, no spaCy, no Hugging Face. The engine uses **TF-IDF vectorization** and **cosine similarity** to match user questions to the closest intent and return a relevant response. Served via a Flask REST API with a sleek dark-themed chat UI.

---

## 🚀 Getting Started

```bash
# 1. Clone the repo
git clone https://github.com/sathvik3429/faq-chatbot-nlp.git
cd faq-chatbot-nlp

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the server
python app.py

# 4. Open in browser
http://localhost:5000
```

---

## 📁 Project Structure

```
faq-chatbot-nlp/
├── app.py              ← Flask REST API server
├── chatbot_engine.py   ← NLP engine (TF-IDF + cosine similarity)
├── intents.json        ← FAQ intents, patterns & responses
├── requirements.txt    ← Dependencies
├── vercel.json         ← Vercel deployment config
└── templates/
    └── index.html      ← Dark-themed chat UI
```

---

## 🧠 How the NLP Works

| Step | What Happens |
|------|-------------|
| 1. Tokenize | Split input, remove stop words and punctuation |
| 2. Stem | Reduce words to root form for better matching |
| 3. TF-IDF | Weight tokens by importance across all intents |
| 4. Cosine Similarity | Find closest matching intent mathematically |
| 5. Respond | Return a random response from matched intent |

> Built entirely with pure Python math (`re`, `math`, `collections`) — no external NLP libraries. This means deeper understanding of how NLP works under the hood.

---

## 🛠️ Tech Stack

| Technology | Role |
|-----------|------|
| Python | NLP engine core |
| Flask | REST API (`/chat`, `/intents`) |
| TF-IDF | Token importance weighting |
| Cosine Similarity | Intent matching |
| HTML / CSS / JS | Chat UI frontend |
| Vercel | Deployment |

---

## 💬 Supported Intents

`greeting` `goodbye` `thanks` `hours` `contact` `pricing` `refund` `features` `account` `password` `about`

### ➕ Adding New Intents

Open `intents.json` and add a block — no retraining needed:

```json
{
  "tag": "shipping",
  "patterns": ["delivery time", "when will it arrive", "how long does shipping take"],
  "responses": ["Standard shipping takes 5–7 business days."]
}
```

Restart the server and it works instantly!

---

## 🔮 Future Upgrades

- [ ] Add Hugging Face sentence transformers for semantic similarity
- [ ] Integrate a database to log and analyze conversations
- [ ] Add multi-turn memory for context-aware responses
- [ ] Train a custom intent classifier with a larger dataset
- [ ] Deploy with a custom domain

---

## 👨‍💻 Author

**Sathvik Rudrarapu**
B.Tech CSE — Jyothishmathi Institute of Technology and Science
📧 rudrarapusathvik@gmail.com | [LinkedIn](https://linkedin.com/in/rudrarapu-sathvik) | [GitHub](https://github.com/sathvik3429)
