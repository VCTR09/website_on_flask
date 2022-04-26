from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about/')
def about():
    return render_template("about.html")

@app.route('/delivery/')
def delivery():
    return render_template("delivery.html")


if __name__ == "__main__":
    app.run(debug=True)

# virtual/bin/python3 Website_on_Flask/script1.py
