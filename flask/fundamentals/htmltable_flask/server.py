from flask import Flask, render_template   # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/lists')
def render_lists():
    # Soon enough, we'll get data from a database, but for now, we're hard coding data
    users = [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'John', 'last_name' : 'Supsupin'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
    return render_template("lists.html", users = users)


# app.run(debug=True) should be the very last statement! 
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
