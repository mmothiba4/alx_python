"""A script that starts a Flask web application:
listening on 0.0.0.0, port 5000"""

from flask import Flask

app = Flask (__name__)

@app.route("/")
def hello_HBNB():
    return "Hello HBNB!"

"""A script that returns a specifeid string hbnb"""

@app.route("/hbnb")
def hbnb():
    return "HBNB"

"""A function that returns a specified string when returning the text in that directory."""
@app.route("/c/<text>")
def c_is_fun():
    return f"C {escape(text)}"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5000")