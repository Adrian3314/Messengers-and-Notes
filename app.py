from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///MessengerAndNotes.db' # 資料庫名稱
db = SQLAlchemy(app) # 建立資料庫物件

@app.route('/') # 路由
@app.route('/home')
def home():
    return render_template('home.html') # 回傳 home.html

if __name__ == '__main__': # 程式進入點
    app.run(debug=True)