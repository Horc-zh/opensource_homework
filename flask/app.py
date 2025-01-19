import flask

app = flask.Flask(__name__)


@app.route("/")
def index():
    return """
    <html>
        <body>
        Welcome to my flask app
        <button onclick="location.href='/form'">Go to Form</button>
        </body>
    </html>"""


@app.route("/form")
def form():
    return flask.render_template("form.html")


@app.route("/hello/<name>")
def hello(name):
    g = globals()
    a = "abc"
    return flask.render_template("hello.html", g=g, a=a)


@app.route("/result", methods=["POST"])
def result():
    return f"""
    <html>
        <body>
            hello, {flask.request.form['fname']}
            <button onclick="location.href='/hello/<my friend>'">Go to Hello</button>
        </body>
    </html>"""


if __name__ == "__main__":
    app.run()
