from app import db

class HistoricalPrice(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    asset_id = db.Column(db.String(4), db.ForeignKey('asset.ticker'), nullable= False)
    timestamp = db.Column(db.Integer, nullable= False)
    daily_high = db.Column(db.Float, nullable=False)
    daily_low = db.Column(db.Float, nullable=False)
    
    asset = db.relationship('Asset', backref=db.backref('historical_prices', lazy= True))