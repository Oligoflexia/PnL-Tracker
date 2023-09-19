from app import db

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    portfolio_id = db.Column(db.Integer, db.ForeignKey('portfolio.id'), nullable= False)
    asset_id = db.Column(db.Integer, db.ForeignKey('asset.id'), nullable= False)
    quantity = db.Column(db.Float, nullable= False)
    transaction_type = db.Column(db.String(10), nullable= False)
    timestamp = db.Column(db.DateTime, nullable= False)
    price_at_time = db.Column(db.Float, nullable= False)

    portfolio = db.relationship('Portfolio', backref=db.backref('transactions', lazy= True))
    asset = db.relationship('Asset', backref=db.backref('transactions', lazy= True))