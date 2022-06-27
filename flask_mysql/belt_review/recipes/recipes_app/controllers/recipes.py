from flask import render_template, redirect, request, session
from recipes_app.models.recipe import Recipe
from recipes_app import app

#######################################################
#             creating and saving
#######################################################
@app.route("/create_recipe")
def create_recipe():
    if not session["logged_in"]:
        return redirect ("/")

    return render_template ("/create_recipe.html")


@app.route("/add_recipe", methods=["POST"])
def add_recipe():
    if not session["logged_in"]:
        return redirect ("/")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$", request.form)
    if not Recipe.valid_recipe(request.form):
        return redirect ("/create_recipe")
    
    data = {
        "name" : request.form["name"],
        "description" : request.form["description"],
        "instruction" : request.form["instruction"],
        "date" : request.form["date"],
        "halfhour" : request.form["halfhour"],
        "user_id" : session["logged_in"]["id"]
    }

    Recipe.save_recipe(data)
    return redirect ("/dashboard")
######################################################

#######################################################
#              editing and updating
#######################################################
@app.route("/edit_a_recipe/<int:id>")
def edit_a_recipe(id):
    if not session["logged_in"]:
        return redirect ("/")

    data = {"id" : id}
    recipe =  Recipe.get_a_recipe(data)
    return render_template ("edit_recipe.html", recipe = recipe)


@app.route("/update_recipe", methods=["POST"])
def update_recipe():
    if not session["logged_in"]:
        return redirect ("/")

    print("##################################", request.form)
    if not Recipe.valid_recipe(request.form):
        return redirect (f"/edit_a_recipe/{request.form['id']}")

    data = {
        "id" : request.form["id"],
        "name" : request.form["name"],
        "description" : request.form["description"],
        "instruction" : request.form["instruction"],
        "date" : request.form["date"],
        "halfhour" : request.form["halfhour"],
        "user_id" : session["logged_in"]["id"]
    }

    Recipe.update_recipe(data)

    return redirect ("/dashboard")
########################################################

#######################################################
#              viewing and deleting
#######################################################

@app.route("/view_a_recipe/<int:id>")
def view_a_recipe(id):
    if not session["logged_in"]:
        return redirect ("/")

    data = {"id" : id}
    recipe =  Recipe.get_a_recipe(data)
    return render_template ("show_recipe.html", recipe =  recipe)


@app.route("/delete_a_recipe/<int:id>")
def delete_recipe(id):
    if not session["logged_in"]:
        return redirect ("/")
    
    data = {"id" : id}
    Recipe.delete_recipe(data)
    return redirect ("/dashboard")









