from app import create_app, db
from models import Asset

eth = Asset(ticker='ETH', name='Ethereum')
btc = Asset(ticker='XBT', name='Bitcoin')



app = create_app()

with app.app_context():
    db.session.add(eth)
    db.session.add(btc)
    
    db.session.commit()