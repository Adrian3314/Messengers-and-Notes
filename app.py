from flask import Flask
from models import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///MessengerAndNotes.db' # 資料庫名稱

db.init_app(app)

from views import *

def init():
    with app.app_context():
        db.create_all()

if __name__ == '__main__': # 程式進入點
    init()
    app.run(debug=True)