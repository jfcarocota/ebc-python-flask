from flask import Flask, request, render_template, url_for, redirect
from database import tasks

app = Flask(__name__)

#si tu ni le dices a route que tipo de metodo http va usar, por default usará un GET
@app.route("/")
def Index():
  return render_template("index.html", todoList = tasks)

@app.route("/newTask", methods=['POST'])
def AddNewTask():
  if request.method == 'POST':
    newTask = {"id": len(tasks) + 1, "name": request.form['task_name']}
    tasks.append(newTask)
    return redirect(url_for('Index'))

if __name__ == "__main__":
  app.run(port=5000, debug=True)