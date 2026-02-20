from flask import Flask, request, jsonify

app = Flask(__name__)

def chatbot_response(message):
    message = message.lower()

    if "hello" in message:
        return "Hi there! 👋"
    elif "how are you" in message:
        return "I'm just code, but I'm doing great!"
    elif "bye" in message:
        return "Goodbye! Have a great day!"
    else:
        return "Sorry, I don't understand that."

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    response = chatbot_response(user_message)

    return jsonify({
        "user_message": user_message,
        "bot_response": response
    })

@app.route("/")
def home():
    return "Chatbot is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
