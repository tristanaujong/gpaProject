from flask import Flask

app = Flask(__name__)

@app.route("/")
def calculator():
    #print("hello chat")
    return "calculate ur grade here"
