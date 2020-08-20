import os
from flask import Flask, request, redirect, url_for, render_template
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["MONGO_DBNAME"] = os.environ.get('MONGO_DBNAME')
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

print(os.getenv('MONGO_URI'))
mongo = PyMongo(app)


@app.route("/")
def show_index():
    """
    renders landing page
    """
    return render_template("pages/index.html")

@app.route('/recipes')
def recipes():
    """
    will render the complete list of recipes
    """
    return render_template("pages/recipes.html",
                           recipes=mongo.db.recipes.find())


@app.route('/recipe/<recipe_id>')
def recipe(recipe_id):
    """
    will show the full details of an individual recipe
    """
    the_recipe = mongo.db.recipes.find_one_or_404({"_id": ObjectId(recipe_id)})
    all_categories = mongo.db.categories.find()
    return render_template('pages/recipe.html', recipe=the_recipe,
                           zcategories=all_categories)


@app.route('/recipe/add', methods=["POST", "GET"])
def add_recipe():
    """
    adds recipe to mongodb collection and then displays to list of recipes page
    """
    recipes = mongo.db.recipes

    if request.method == "POST":
        recipes.insert_one(request.form.to_dict())
        return redirect(url_for('see_our_recipes'))

    return render_template("pages/addrecipe.html",
                           categories=mongo.db.categories.find())


@app.route('/edit/recipe/<recipe_id>')
def edit_recipe(recipe_id):
    """
    will allow the user to edit a particular recipe. Recipe reposted on submit
    """
    the_recipe = mongo.db.recipes.find_one_or_404({"_id": ObjectId(recipe_id)})
    all_categories = mongo.db.categories.find()
    return render_template('pages/editrecipe.html', recipe=the_recipe,
                           categories=all_categories)


@app.route('/update/recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    """
    updates edited recipes to mongo.db and displays on see our recipes
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
    return redirect(url_for('recipes'))


@app.route('/delete/recipe/<recipe_id>')
def delete_recipe(recipe_id):
    """
    allow user to delete any recipe
    """
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    return redirect(url_for('recipes'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
