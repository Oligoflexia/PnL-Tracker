from app import db
from sqlalchemy import UniqueConstraint

class Asset(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    ticker = db.Column(db.String(4), nullable= False)
    name = db.Column(db.String(128), nullable= False)
    
    __table_args__ = (UniqueConstraint('ticker', name='uix_ticker'),)
    
