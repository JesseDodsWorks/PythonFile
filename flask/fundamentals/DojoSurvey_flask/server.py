
from flask import Flask, render_template, request, redirect, session  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def Onindex():
    print("index POPPED")
    return render_template ('index.html') 

@app.route("/passinfo", methods=["POST"])
def passinfo():
    session["nameValue"] = request.form["name"]
    session["locationValue"] = request.form["location"]
    session["languageValue"] = request.form["language"]
    session["commentValue"] = request.form["comment"]


    return redirect("/result")

@app.route('/result')
def Oninfo():
    print("info POPPED")
    return render_template ('info.html') 

@app.route("/clear")
def clear():
    session.clear()
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)

