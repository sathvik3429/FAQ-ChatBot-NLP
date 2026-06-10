"""
app.py
Flask web server for the FAQ Chatbot.
Run: python app.py
Then open: http://localhost:5000
"""

from flask import Flask, request, jsonify, render_template
from chatbot_engine import IntentClassifier
import os

app = Flask(__name__)
bot = IntentClassifier("intents.json")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message", "").strip()
    if not user_input:
        return jsonify({"error": "Empty message"}), 400
    result = bot.chat(user_input)
    return jsonify(result)

@app.route("/intents", methods=["GET"])
def get_intents():
    """Returns list of available intent tags — useful for debugging."""
    tags = [i["tag"] for i in bot.intents]
    return jsonify({"intents": tags, "count": len(tags)})

if __name__ == "__main__":
    print("Starting FAQ Chatbot server...")
    print("Open http://localhost:5000 in your browser\n")
    app.run(debug=True, port=5000)
