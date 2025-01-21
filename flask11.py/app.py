from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("add.html")


@app.route("/add", methods=["POST"])
def add():
    value1 = request.form.get("value1", 0)
    value2 = request.form.get("value2", 0)
    value1 = int(value1) if value1.isdigit() else 0
    value2 = int(value2) if value2.isdigit() else 0
    result = value1 + value2
    return f"Result: {result}"


if __name__ == "__main__":
    app.run()
