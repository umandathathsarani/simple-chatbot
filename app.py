import json
import random
from datetime import datetime
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def load_support_rules():
    with open("responses.json", "r") as file:
        return json.load(file)

def log_chat(user_message, bot_response):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open("chat_log.txt", "a") as log_file:
        log_file.write(f"[{timestamp}] User: {user_message}\n")
        log_file.write(f"[{timestamp}] Bot: {bot_response}\n")
        log_file.write("-" * 40 + "\n")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    payload = request.get_json()
    user_message = payload.get("message", "").lower().strip()
    
    data = load_support_rules()
    rules = data.get("rules", {})
    fallback = data.get("fallback", [])
    
    bot_reply = random.choice(fallback)

    for keyword, responses in rules.items():
        if keyword in user_message:
            bot_reply = random.choice(responses)
            break 
        
    log_chat(user_message, bot_reply)
            
    return jsonify({"response": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)