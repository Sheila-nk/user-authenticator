from flask import render_template

from user_authenticator import app

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")
