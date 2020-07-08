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
@app.route('/get_recipes')
def get_recipes():
    return render_template("landingpage.html", recipes=mongo.db.recipes.find())

@app.route('/search_recipes')
def search_recipes():
    recipes=mongo.db.recipes.find()
    return render_template("/searchrecipes.html")

@app.route('/display_recipe')
def display_recipe():
    return render_template("displayrecipe.html", recipes=mongo.db.recipes.find())



@app.route('/add_recipe')
def add_recipe():
    return render_template("addrecipe.html", categories=mongo.db.categories.find())
    
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes=mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('show_recipe')) 
     # only redirected to show_recipe for test purposes 

@app.route('/show_recipe/<recipe_id>')
def show_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipes_id)})
    all_recipes = mongo.db.recipes.find()
    return render_template("showrecipe.html", recipe=the_recipe,
                                recipes=all_recipes)

@app.route('/edit_task/<task_id>')
def edit_task(task_id):
    the_task =  mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
    all_categories =  mongo.db.categories.find()
    return render_template('edittask.html', task=the_task,
                           categories=all_categories)

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)

