import json
import bcrypt
from core import db, Product, Vendor, Category, Address

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
    categories = [{'id': c.id, 'name': c.name, 'description': c.description, 'image': c.image} for c in catQuery ]
    return categories


def getAllProducts():
    prodQuery = Product.query.all()
    products = [{
        'id':p.id,
        'name': p.name,
        'vendor': Vendor.query.filter_by(id=p.vendor_id).first().name,
        'category': Category.query.filter_by(id=p.category_id).first().name,
        'price': p.price
    } for p in prodQuery]
    return products


def getAllVendors():
    vendQuery = Vendor.query.all()
    vendors = [{
        'name': v.name,
        'street': Address.query.filter_by(user_id=v.user_id).first().street_name,
        'city': Address.query.filter_by(user_id=v.user_id).first().city,
        'state': Address.query.filter_by(user_id=v.user_id).first().state,
        'zip': Address.query.filter_by(user_id=v.user_id).first().zip_code,
    } for v in vendQuery]
    return vendors

def seedCategories():
    with open('/home/adempus/Projects/BCHackathon/Fleetmart/src/server/seeds/categories.json', 'r') as jsonFile:
        data = json.load(jsonFile)
        for i in data:
            newCategory = Category(i['name'], i['description'], i['image'])
            db.session.add(newCategory)
            db.session.commit()
