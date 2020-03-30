import markdown
import os
import shelve

# Import the framework
from flask import Flask, g
from flask_restful import Resource, Api, reqparse

# Create an instance of Flask
app = Flask(__name__)

# Create the API
api = Api(app)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = shelve.open("items.db")
    return db

@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def index():
    """README Documentation"""

    # Open the README file
    with open(os.path.dirname(app.root_path) + '/README.md', 'r') as readme_file:

        # Read file
        content = readme_file.read()

        # Convert to HTML
        return markdown.markdown(content)


class ItemList(Resource):
    def get(self):
        shelf = get_db()
        keys = list(shelf.keys())

        items = []

        for key in keys:
            items.append(shelf[key])

        return {'message': 'Success', 'data': items}, 200

    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('identifier', required=True)
        parser.add_argument('name', required=True)
        parser.add_argument('item_type', required=True)
        parser.add_argument('item_genre', required=False)

        # Parse the arguments into an object
        args = parser.parse_args()

        shelf = get_db()
        shelf[args['identifier']] = args

        return {'message': 'Item added', 'data': args}, 201


class Item(Resource):
    def get(self, identifier):
        shelf = get_db()

        # If the key does not exist in the data store, return a 404 error.
        if not (identifier in shelf):
            return {'message': 'Item not found', 'data': {}}, 404

        return {'message': 'Item found', 'data': shelf[identifier]}, 200

    def delete(self, identifier):
        shelf = get_db()

        # If the key does not exist in the data store, return a 404 error.
        if not (identifier in shelf):
            return {'message': 'Item not found', 'data': {}}, 404

        del shelf[identifier]
        return '', 204


api.add_resource(ItemList, '/items')
api.add_resource(Item, '/items/<string:identifier>')




