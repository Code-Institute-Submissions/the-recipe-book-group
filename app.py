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
    return render_template("recipes.html", recipes=mongo.db.recipes.find())
    


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)

