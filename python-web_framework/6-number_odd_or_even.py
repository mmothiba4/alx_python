"""A script that starts a Flask web application:
listening on 0.0.0.0, port 5000"""

from flask import Flask
from flask import render_template

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
    return f"C" + text.replace('_', ' ')

@app.route("/python/<text>")
def python_is_cool(text="is cool"):
    """Templates used to generate any type of text file.
    """
    return f"Python " + text.replace('_', ' ')

@app.route("/number/<int:n>", strict_slashes=False)
def is_a_num(n):
    return f"{n} is a number"

@app.route("/number_template/<int:n>", strict_slashes= False)
def number_template(n):
    return render_template("5-number.html", n = n)

@app.route("/number_odd_or_even/<int:n>", strict_slashes= False)
def number_odd_or_even(n):
    return render_template("6-number_odd_or_even.html", n=n)



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5000")