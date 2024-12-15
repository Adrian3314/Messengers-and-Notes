from flask import Flask
from flask_login import LoginManager
from models import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///MessengerAndNotes.db' # 資料庫名稱
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'messengerandnotes'

db.init_app(app)

from views import *

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

def init():
    with app.app_context():
        db.create_all()

if __name__ == '__main__': # 程式進入點
    init()
    app.run(debug=True)