from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    text = ""
    if request.method == 'POST':
        text = request.form['user_text']
        pages = text.split("\n\n")  # Split text into "pages" by double newlines
        return render_template('flipbook.html', pages=pages)
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
