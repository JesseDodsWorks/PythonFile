
from flask import Flask, render_template, request , redirect, session   # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes


@app.route('/')
def main():
    print("BASICLY RUNNING V1")
    print(session)

    if not "number" in session:
        session["number"] = 0
    else:
        session["number"] += 1
    return render_template ('index.html')

@app.route("/addnumber")
def added_count():
    print("BASICLY RUNNING v2")
    session["number"] += 1
    return redirect ("/")

@app.route("/destroy_session")
def clear_views():
    session.clear()
    return redirect("/")

# app.run(debug=True) should be the very last statement! 
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.