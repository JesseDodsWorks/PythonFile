from flask import Flask, render_template, redirect, request, session  # Import Flask to allow us to create our app
from friend import Friend
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route("/")
def index():
    # call the get all classmethod to get all friends
    friends = Friend.get_all()
    print(friends)
    return render_template("index.html", all_friends = friends)

@app.route('/create_friend', methods=["POST"])
def create_friend():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "occ" : request.form["occ"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    Friend.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/')




if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

