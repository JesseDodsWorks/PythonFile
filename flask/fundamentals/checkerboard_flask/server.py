from flask import Flask, render_template  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

# FIRST CHALLENGE *********************

@app.route('/')          
def index():
    return render_template( "index.html", phrase="THE BEST CODER AROUND")

# SECOND CHALLENGE ******************

@app.route('/<int:X>')         
def matchinggrid(X):
    return render_template( "matchinggrid.html", X=X)

# THIRD CHALLENGE **********************

@app.route('/<int:X>/<int:Y>')         
def changegrid(X, Y):
    return render_template( "changegrid.html", X=X, Y=Y)

# NINJA CHALLENGE

@app.route('/<int:X>/<int:Y>/<string:color1>/<string:color2>')          
def colorgrid(X, Y, color1, color2):
    return render_template( "colorchanger.html", X=X, Y=Y, color1=color1, color2=color2)




if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    

    app.run(debug=True)    # Run the app in debug mode.

