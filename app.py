from flask import Flask, request, render_template

app = Flask(__name__)

#si tu ni le dices a route que tipo de metodo http va usar, por default usará un GET
@app.route("/")
def Index():
  return render_template("index.html")
  #return "hello world flask"
  #return "<h1>hello world flask</h1>"
  #return "<a href='#'>hello world flask</a>"

#@app.route("/ebc")
#def HolaEBC():
#  return "Hola ebc"
#
#@app.route("/ebc/random")
#def UnGetRandom():
#  return "Hola ebc random"

#@app.route("/", methods=['POST'])
#def AddNewTask():
#  if request.method == 'POST':
    

if __name__ == "__main__":
  app.run(port=5000, debug=True)