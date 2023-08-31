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
def c_is_fun(text="is fun"):
    return f"C " + text.replace ('_', ' ')

@app.route("/python/<text>")
def python_is_cool(text= "is cool"):
    """Templates used to generate any type of text file.
    """
    return f"Python " + text.replace('_', ' ')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5000")