from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    username = db.Column(db.String(80), unique=True, nullable= False)
    hashed_password = db.Column(db.String(128), nullable= False)
    email = db.Column(db.String(120), unique=True, nullable= False)
    