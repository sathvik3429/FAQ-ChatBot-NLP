import os
from flask import Flask, request, jsonify, render_template
from chatbot_engine import IntentClassifier

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
    tags = [i["tag"] for i in bot.intents]
    return jsonify({"intents": tags, "count": len(tags)})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=False)