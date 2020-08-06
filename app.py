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


@app.route("/")
def show_index():
    return render_template("index.html")


@app.route('/addrecipe')
def add_recipe():
    return render_template("addrecipe.html", categories=mongo.db.categories.find())


@app.route('/insertrecipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('recipe_list'))


@app.route('/recipelist')
def recipe_list():
    return render_template("recipelist.html", recipes=mongo.db.recipes.find())


@app.route('/recipepage/ <recipe_id>')
def show_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template('recipepage.html', recipe=the_recipe)


@app.route('/editrecipe/ <recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_categories = mongo.db.categories.find()
    return render_template('editrecipe.html', recipe=the_recipe, categories=all_categories)


@app.route('/updaterecipe/ <recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
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
    return redirect(url_for('recipe_list'))


@app.route('/deleterecipe/ <recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    return redirect(url_for('recipe_list'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
