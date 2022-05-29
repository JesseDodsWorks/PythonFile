from flask import Flask, render_template   # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following

def index():
    return render_template("index.html")  # Return the string 'Hello World!' as a response
# import statements, maybe some other routes
    
@app.route('/dojo')
def dojo():
  return "Dojo!"

@app.route('/say/<name>') # for a route '/say/____' anything after '/hello/' gets passed as a variable 'name'
def say(name):
    return "Hi " + name + "!"


@app.route("/repeat/<string:name>/<int:times>")
def repeat(name,times):
    return render_template("hello.html", phrase="YOOOOOO", name=name, times=times)


# app.run(debug=True) should be the very last statement! 
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
