from flask import Flask
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///MessengerAndNotes.db' # 資料庫名稱
db = SQLAlchemy() # 建立資料庫物件

class User(UserMixin, db.Model): # 使用者資料表
    def __init__(self, user_ID, name, password):
        self.user_ID = user_ID
        self.name = name
        self.password = password

    user_ID = db.Column(db.Integer, primary_key=True) # 使用者編號
    name = db.Column(db.String(100)) # 使用者名稱
    password = db.Column(db.String(100)) # 使用者密碼

    __tablename__ = 'user' # 資料表名稱

    def get_id(self):
        return self.user_ID

class Note(db.Model): # 筆記資料表
    def __init__(self, note_ID, content, time, user_ID):
        self.note_ID = note_ID
        self.content = content
        self.time = time
        self.user_ID = user_ID

    note_ID = db.Column(db.Integer, primary_key=True) # 便利貼編號
    content = db.Column(db.String(1000)) # 便利貼內容
    time = db.Column(db.DateTime, default = datetime.now) # 便利貼時間
    user_ID = db.Column(db.Integer, db.ForeignKey('user.user_ID')) 

    __tablename__ = 'note' # 資料表名稱

class Message(db.Model): # 訊息資料表
    def __init__(self, room_no, time, message):
        self.room_no = room_no
        self.time = time
        self.message = message

    room_no = db.Column(db.Integer, db.ForeignKey('room.room_no'), primary_key=True) # 聊天室編號
    time = db.Column(db.DateTime, default = datetime.now, primary_key=True) # 訊息時間
    message = db.Column(db.String(1000)) # 訊息內容

    __tablename__ = 'message' # 資料表名稱

class Room(db.Model): # 聊天室資料表
    def __init__(self, room_no, user_ID1, user_ID2):
        self.room_no = room_no
        self.user_ID1 = user_ID1
        self.user_ID2 = user_ID2

    room_no = db.Column(db.Integer, primary_key=True) # 聊天室編號
    user_ID1 = db.Column(db.Integer, db.ForeignKey('user.user_ID')) # 使用者編號1
    user_ID2 = db.Column(db.Integer, db.ForeignKey('user.user_ID')) # 使用者編號2

    __tablename__ = 'room' # 資料表名稱