from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_migrate import Migrate

from core import db, getAppKey, getDBCredentials, seedCategories, getAllCategories, getAllProducts, getAllVendors

DEBUG = True


def create_app():
    appInstance = Flask(__name__)
    appInstance.config.from_object(__name__)
    # CORS setup
    CORS(appInstance, resources={r'/*': {'origins': '*'}})
    appInstance.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    appInstance.config['SQLALCHEMY_DATABASE_URI'] = getDBCredentials(
        'db_credentials.json'
    )
    appInstance.config['SECRET_KEY'] = getAppKey('app_key.json')
    return appInstance


app = create_app()
app.app_context().push()
# database initialization
db.init_app(app)
migrate = Migrate(app, db)

seed = False
if seed:
    seedCategories()


@app.route('/', methods=['GET'])
def homeRoute():
    return "welcome"

@app.route('/test_route', methods=['GET'])
def testRoute():
    testData = {'A': 1, 'B': 2, 'C': 3 }
    return jsonify(testData)


@app.route('/categories', methods=['GET'])
def getCategories():
    categories = getAllCategories()
    print(f"categories: {categories}")
    return jsonify(categories)


@app.route('/products', methods=['GET'])
def getProducts():
    products = getAllProducts()
    print(f"products: {products}")
    return jsonify(products)


@app.route('/vendors', methods=['GET'])
def getVendors():
    vendors = getAllVendors()
    print(f"vendors: {vendors}")
    return jsonify(vendors)


