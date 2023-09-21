from app import db
from sqlalchemy import UniqueConstraint

class User(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    username = db.Column(db.String(80), nullable= False)
    hashed_password = db.Column(db.String(128), nullable= False)
    email = db.Column(db.String(120), nullable= False)
    
    __table_args__ = (UniqueConstraint('username', name='uix_username'),
                      UniqueConstraint('email', name='uix_email'))
