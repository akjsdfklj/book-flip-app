from flask import Flask, render_template, request
import openai
import os

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = os.environ.get("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")

@app.route("/", methods=["GET", "POST"])
def index():
    generated_text = ""
    if request.method == "POST":
        prompt = request.form["prompt"]
        response = openai.ChatCompletion.create(
            model="gpt-4o",  # or "gpt-4" or "gpt-3.5-turbo"
            messages=[{"role": "user", "content": prompt}]
        )
        generated_text = response.choices[0].message.content
    return render_template("index.html", generated_text=generated_text)

if __name__ == "__main__":
    app.run(debug=True)
