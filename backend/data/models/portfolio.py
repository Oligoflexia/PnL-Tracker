from . import db

class Portfolio(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable= False)
    name = db.Column(db.String(128), nullable= False)

    user = db.relationship('User', backref=db.backref('portfolios', lazy= True))