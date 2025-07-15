from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
CORS(app)

def load_docs():
    docs_dir = "docs"
    contents = ""
    for file in os.listdir(docs_dir):
        if file.endswith(".md"):
            with open(os.path.join(docs_dir, file), "r", encoding="utf-8") as f:
                contents += f"\n\n" + f.read()
    return contents

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    task_type = data.get("task", "general")
    content = data.get("content", "")
    
    docs = load_docs()
    full_prompt = f"{docs}\n\nTâche : {task_type.upper()}\nContenu :\n{content}"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": full_prompt}],
            temperature=0.5
        )
        return jsonify({"response": response['choices'][0]['message']['content']})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
