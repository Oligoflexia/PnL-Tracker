from . import db

class Asset(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    ticker = db.Column(db.String(4), unique= True, nullable= False)
    name = db.Column(db.String(128), nullable= False)
    
