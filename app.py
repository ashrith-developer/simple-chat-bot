from flask import Flask, request, jsonify

app = Flask(__name__)

# Simple rules for chatbot replies
responses = {
    "sad": "I’m sorry you’re feeling sad 💙. Remember, tough times don’t last, but tough people do.",
    "happy": "That’s amazing! 🌟 Keep spreading positivity.",
    "angry": "It’s okay to feel angry 😔. Try taking a deep breath and going for a short walk.",
    "stressed": "Stress is normal. 🧘 Take a break, drink some water, and relax for a moment.",
    "lonely": "You are not alone 💜. Reach out to a friend or loved one, even a short chat can help.",
    "default": "I’m here to listen. Tell me more about how you feel."
}

@app.route("/")
def home():
    return "💬 Welcome to the Mental Health Chatbot API!"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message", "").lower()

    reply = responses.get("default")
    for key in responses.keys():
        if key in message:
            reply = responses[key]
            break

    return jsonify({"user_message": message, "chatbot_reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
