from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from sqlalchemy import create_engine, MetaData

app = Flask(__name__)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(BASE_DIR, 'data', 'db', 'test.db')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

migrate = Migrate(app, db)

from data.models import Asset, HistoricalPrice, Portfolio, Transaction, User

def create_tables():
    db.create_all()

engine = create_engine('sqlite:///' + db_path)
meta = MetaData()
meta.reflect(bind=engine)

for table in meta.tables:
    print("Table:", table)
    for column in meta.tables[table].c:
        print("Column:", column)
        

@app.route('/test')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug= True)


