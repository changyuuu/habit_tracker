from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

habits = ["Test habit"]


@app.route("/")
def index():
  return render_template("index.html", habits=habits,  title="Home")

@app.route("/add", methods=["GET","POST"])
def add_habit():
  
  if request.method == "POST":
    habit = request.form.get("habit")
    habits.append(habit)
    return redirect(url_for(request.url))
    
  return render_template("add_habit.html",title="Add Habit")


if __name__ == "__main__":
  app.run(debug=True)