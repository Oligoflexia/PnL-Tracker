from app import create_app, db
from models import Asset, HistoricalPrice
import pandas as pd
import os

#create records for asset table
eth = Asset(ticker='ETH', name='Ethereum')
btc = Asset(ticker='XBT', name='Bitcoin')

#create records for historical price
columns = [0, 2, 3]
column_names = ['unix_timetamp', 'high', 'low']

current_dir = os.path.abspath(os.path.dirname(__file__))
btc_data_path = 'data/raw/XBT_OHLCVT'
btc_data_file = 'XBTCAD_1440.csv'

eth_data_path = 'data/raw/ETH_OHLCVT'
eth_data_file = 'ETHCAD_1440.csv'

btc_csv_path = os.path.join(current_dir, btc_data_path, btc_data_file)
eth_csv_path = os.path.join(current_dir, eth_data_path, eth_data_file)

btc_data = pd.read_csv(btc_csv_path, usecols=columns, names=column_names, skiprows=1)
eth_data = pd.read_csv(eth_csv_path, usecols=columns, names=column_names, header=None)

#fill out the tables
app = create_app()

with app.app_context():
    #Add assets
    db.session.add(eth)
    db.session.add(btc)
    
    #Add historical price data
    for row in btc_data.values:
        date = row[0]
        high = row[1]
        low = row[2]
        
        db.session.add(HistoricalPrice(asset_id='XBT', 
                                       timestamp=date,
                                       daily_high=high,
                                       daily_low=low))
        
    for row in eth_data.values:
        date = row[0]
        high = row[1]
        low = row[2]
        
        db.session.add(HistoricalPrice(asset_id='ETH', 
                                        timestamp=date,
                                        daily_high=high,
                                        daily_low=low))
        
    
    db.session.commit()