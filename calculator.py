from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def calculator():
    return render_template("frontpage.html") # on this page, it renders the frontpage html
