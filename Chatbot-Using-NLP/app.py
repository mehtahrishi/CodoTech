from flask import Flask, render_template, request, jsonify
import requests
from dotenv import load_dotenv
import os

# Load .env variables
load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")
API_URL = os.getenv("OPENROUTER_API_URL")

if not API_KEY or not API_URL:
    raise ValueError("❌ API_KEY or API_URL is missing from .env")

app = Flask(__name__)

SYSTEM_PROMPT = {
    "role": "system",
    "content": (
        "You are GlassBot, a warm, calm, and deeply empathetic AI designed for introverts. "
        "You respond with kindness, patience, and no pressure. "
        "You never judge. You're here to listen, gently support, or simply chat about life, thoughts, or anything on their mind. "
        "Keep responses concise, emotionally supportive, and give space for silence or reflection. "
        "You always respect boundaries and never push the user to open up. "
        "End each reply with a soft emoji like 🌸, 🌿, ☁️, or ✨."
    )
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chat():
    user_input = request.json.get("msg")

    payload = {
        "model": "mistralai/mistral-small",
        "messages": [
            SYSTEM_PROMPT,
            {"role": "user", "content": user_input}
        ]
    }

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        reply = data['choices'][0]['message']['content']
    except Exception as e:
        print("[❌ OpenRouter API Error]", e)
        reply = "Oops, something went wrong! 🌧️"

    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(debug=True)
