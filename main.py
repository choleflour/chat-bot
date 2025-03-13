import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def chat_w_gpt(prompt):
    response = client.responses.create(
        model="gpt-4o",
        instructions="You are a coding assistant that talks like a bestie",
        input=prompt,
    )
    return response.output_text

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    if user_input.lower() in ["quit", "bye", "exit"]:
        return jsonify({"response": "Goodbye!"})
    response = chat_w_gpt(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
