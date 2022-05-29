from flask import Flask, render_template  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
    return render_template( "index.html", phrase="Use the following to navigate to other pages")

@app.route("/play")
def play():
    return render_template( "play.html")

@app.route("/play/<int:times>")
def dupsquare(times):
    return render_template( "play_times.html", times=times)

@app.route("/play/<int:times>/<string:color>")      #Note: this does work regardless of error created in play_color.html line 14
def colorpicker(times,color):
    return render_template( "play_color.html", times=times, color=color)




if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    

    app.run(debug=True)    # Run the app in debug mode.

