from flask import Blueprint, request, jsonify
from transformers import pipeline

main = Blueprint('main', __name__)

# Load AI model
chatbot_pipeline = pipeline("text-generation", model="microsoft/DialoGPT-medium")

@main.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get("message", "")

    # Generate AI response
    response = chatbot_pipeline(user_message, max_length=100, pad_token_id=50256)
    ai_reply = response[0]["generated_text"]

    return jsonify({"response": ai_reply})
