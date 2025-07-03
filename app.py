from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = "YOUR_API_KEY"

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
