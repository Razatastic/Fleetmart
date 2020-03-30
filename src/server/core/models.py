from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    first_name = db.Column(db.String(75), unique=False, nullable=False)
    last_name = db.Column(db.String(75), unique=False, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    is_vendor = db.Column(db.Boolean, nullable=False)
    address = db.relationship('Address', backref='user', lazy=True)
    vendor = db.relationship('Vendor', backref='user', lazy=True)

    def __init__(self, first_name, last_name, email, password, is_vendor):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.is_vendor = is_vendor

    def __repr__(self):
        return '<User %r>' % self.email


class Address(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    street_name = db.Column(db.String(75), unique=False, nullable=False)
    city = db.Column(db.String(70), unique=False, nullable=False)
    state = db.Column(db.String(70), unique=True, nullable=False)
    zip_code = db.Column(db.String(70), unique=True, nullable=False)
    apt = db.Column(db.String(10), unique=False, nullable=False)
    user_id = db.Column(db.BigInteger, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, street_name, city, state, zip_code, apt, user_id):
        self.street_name = street_name,
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.apt = apt
        self.user_id = user_id

    def __repr__(self):
        return '<Address %r>' % self.street_name


class Vendor(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(100), unique=False, nullable=False)
    user_id = db.Column(db.BigInteger, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def __repr__(self):
        return '<Vendor %r>' % self.name


class Product(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(100), unique=False, nullable=False)
    price = db.Column(db.Float, nullable=False)
    category_id = db.Column(db.BigInteger, db.ForeignKey('category.id'), nullable=False)
    vendor_id = db.Column(db.BigInteger, db.ForeignKey('vendor.id'), nullable=False)

    def __init__(self, name, price, category_id, vendor_id):
        self.name = name
        self.price = price,
        self.category_id = category_id
        self.vendor_id = vendor_id

    def __repr__(self):
        return '<Product %r>' % self.name


class Category(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(75), unique=True)
    description = db.Column(db.String(75), unique=True)
    products = db.relationship('Product', backref='category', lazy=True)

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return '<Category %r>' % self.name
