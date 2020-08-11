import os
from flask import Flask, request, redirect, url_for, render_template
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'recipe_cook_book_group'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

print(os.getenv('MONGO_URI'))
mongo = PyMongo(app)


# landing page
@app.route("/")
def show_index():
    """
    reders landing page
    """
    return render_template("pages/index.html")


@app.route('/testextend')
def extend():
    return render_template("testextend.html")


# Adding/posting recipe
@app.route('/recipe/add', methods=["POST", "GET"])
def add_recipe():
    """
    adds recipe to mongodb collection and then displays to list of recipes page
    """
    recipes = mongo.db.recipes

    if request.method == "POST":
        recipes.insert_one(request.form.to_dict())
        return redirect(url_for('pages/recipe_list'))

    return render_template("pages/addrecipe.html",
                           categories=mongo.db.categories.find())


# list of recipes
@app.route('/recipelist')
def recipe_list():
    """
    will render the complete list of recipes
    """
    return render_template("pages/recipelist.html",
                           recipes=mongo.db.recipes.find())


# recipe page
@app.route('/recipepage/ <recipe_id>')
def show_recipe(recipe_id):
    """
    will show the full details of an individual recipe
    """
    the_recipe = mongo.db.recipes.find_one_or_404({"_id": ObjectId(recipe_id)})
    all_categories = mongo.db.categories.find()
    return render_template('pages/recipepage.html', recipe=the_recipe,
                           zcategories=all_categories)


# edit recipe
@app.route('/editrecipe/ <recipe_id>')
def edit_recipe(recipe_id):
    """
    will allow the user to edit a particular recipe. Recipe reposted on submit
    """
    the_recipe = mongo.db.recipes.find_one_or_404({"_id": ObjectId(recipe_id)})
    all_categories = mongo.db.categories.find()
    return render_template('pages/editrecipe.html', recipe=the_recipe,
                           categories=all_categories)


# update recipe
@app.route('/updaterecipe/ <recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    """
    updates edited recipes to mongo.db and displays on recipe list
    """
    recipes = mongo.db.recipes
    recipes.update({'_id': ObjectId(recipe_id)},
                   {
        'recipe_name': request.form.get('recipe_name'),
        'category_name': request.form.get('category_name'),
        'added_by': request.form.get('added_by'),
        'serves': request.form.get('serves'),
        'prep_time': request.form.get('prep_time'),
        'cooking_time': request.form.get('cooking_time'),
        'ingredients': request.form.get('ingredients'),
        'instructions': request.form.get('instructions')
    })
    return redirect(url_for('pages/recipe_list'))


# delete recipe
@app.route('/deleterecipe/ <recipe_id>')
def delete_recipe(recipe_id):
    """
    allow user to delete any recipe
    """
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    return redirect(url_for('pages/recipe_list'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
