from flask import Flask, render_template
from dice_logic import roll_die

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", result=None,exit_game=None)

@app.route("/roll")
def roll():
    d1, d2 =  roll_die()
    result = f"({d1} {d2})"
    return render_template("index.html", result=result,exit_game=None)

@app.route("/exit")
def exit_game():
    return render_template("index.html",result=None, exit_msg="Thanks for playing Game")

if __name__ == "__main__":
    app.run(debug=True)
