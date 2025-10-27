from flask import Flask, render_template, request, jsonify
from transformers import pipeline

app = Flask(_name_)
chatbot = pipeline("text-generation", model="gpt2")

@app.route("/")
def home():
    return "Hello! I'm your digital personality clone 🤖"

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]
    response = chatbot(user_message, max_length=100, do_sample=True)[0]["generated_text"]
    return jsonify({"reply": response})

if _name_ == "_main_":
    app.run(debug=True)
