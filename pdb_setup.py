print('lets start a db')
print('🌶️')

peppers = '🌶️🌶️🌶️🌶️🌶️🌶️'
print(int(len(peppers)/2))

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\sqlite\\library.db'

db = SQLAlchemy(app)
db.init_app(app)