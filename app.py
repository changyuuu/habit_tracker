from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html", title="Home")

@app.route("/add", methods=["GET","POST"])
def add_habit():
  return render_template("add_habit.html",title="Add Habit")


if __name__ == "__main__":
  app.run(debug=True)