from transformers import pipeline

# Load chatbot model using text-generation
chatbot_pipeline = pipeline("text-generation", model="microsoft/DialoGPT-medium")

def get_chatbot_response(user_input):
    response = chatbot_pipeline(user_input, max_length=100, pad_token_id=50256)
    return response[0]["generated_text"]  # Extract chatbot response
