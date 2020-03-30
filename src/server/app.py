from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_migrate import Migrate


from core import db, getAppKey, getDBCredentials

DEBUG = True


def create_app():
    appInstance = Flask(__name__)
    appInstance.config.from_object(__name__)
    # CORS setup
    CORS(appInstance, resources={r'/*': {'origins': '*'}})
    appInstance.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    appInstance.config['SQLALCHEMY_DATABASE_URI'] = getDBCredentials(
        '/home/adempus/Projects/BCHackathon/Fleetmart/src/server/db_credentials.json'
    )
    appInstance.config['SECRET_KEY'] = getAppKey('/home/adempus/Projects/BCHackathon/Fleetmart/src/server/app_key.json')
    return appInstance


app = create_app()
app.app_context().push()
# database initialization
db.init_app(app)
migrate = Migrate(app, db)


@app.route('/test_route', methods=['GET'])
def testRoute():
    testData = {'A': 1, 'B': 2, 'C': 3 }
    return jsonify(testData)
