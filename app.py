import json
import random
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def load_support_rules():
    with open("responses.json", "r") as file:
        return json.load(file)

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
    
    for keyword, responses in rules.items():
        if keyword in user_message:
            return jsonify({"response": random.choice(responses)})
            
    return jsonify({"response": random.choice(fallback)})

if __name__ == "__main__":
    app.run(debug=True)