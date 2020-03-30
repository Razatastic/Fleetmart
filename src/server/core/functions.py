import json
import bcrypt
from core import db, Category

def getDBCredentials(path):
    with open(path, 'r') as jsonFile:
        data = json.load(jsonFile)
    return f"{data['driver']}://{data['user']}:{data['password']}@{data['host']}:{data['port']}/{data['db']}"

def getAppKey(path):
    with open(path, 'r') as jsonFile:
        data = json.load(jsonFile)
    return data['app_key']


def getAllCategories():
    catQuery = Category.query.all()
    categories = [{ 'id': c.id, 'name': c.name, 'description': c.description } for c in catQuery ]
    return categories


def seedCategories():
    with open('/home/adempus/Projects/BCHackathon/Fleetmart/src/server/seeds/categories.json', 'r') as jsonFile:
        data = json.load(jsonFile)
        for k in data.items():
            name, desc = k[0], k[1]
            print(f'data: {name}: {desc}')
            newCategory = Category(name, desc)
            db.session.add(newCategory)
            db.session.commit()


