from flask import render_template, redirect, request, session
from DojoSurvey_app import app
from DojoSurvey_app.models.dojo import Dojo


@app.route('/')
def Onindex():  
    return render_template ('index.html') 

@app.route("/passinfo", methods=["POST"])
def passinfo():
    print(request.form)
    if not Dojo.validate_dojo(request.form):
        return redirect ("/")
        
    Dojo.save(request.form)
    return redirect("/result")

@app.route('/result')
def Oninfo():
    print("info POPPED")
    return render_template ('info.html', dojo = Dojo.get_dojo()) 
