from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return "<h1>welcome to home!...</h1>"

@app.route("/about")
def about():
    return "about"

if __name__ == "__main__":
    app.run(debug=True)