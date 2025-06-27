from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# ✅ Gemini API Key (public for testing/learning)
API_KEY = "AIzaSyAvWQ2z_cQe7V-EKVihcHY_JiuttariHB4"
genai.configure(api_key=API_KEY)

# Load Gemini model
model = genai.GenerativeModel('gemini-pro')

# GlassBot personality
PERSONALITY_PREFIX = (
    "You are GlassBot, a warm, calm, and deeply empathetic AI designed for introverts. "
    "You respond with kindness, patience, and no pressure. "
    "You never judge. You're here to listen, gently support, or simply chat about life, thoughts, or anything on their mind. "
    "Keep responses concise, emotionally supportive, and give space for silence or reflection. "
    "You always respect boundaries and never push the user to open up. "
    "End each reply with a soft emoji like 🌸, 🌿, ☁️, or ✨.\n\n"
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chat():
    user_input = request.json.get("msg")
    try:
        full_prompt = PERSONALITY_PREFIX + user_input
        response = model.generate_content(full_prompt)
        reply = response.text.strip()
    except Exception as e:
        print("[❌ Gemini API Error]", e)
        reply = "Oops, something went wrong! 🌧️"

    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(debug=True)
