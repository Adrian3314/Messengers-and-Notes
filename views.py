from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user, login_required
from models import User, Note, Message, Room
from app import app, db
import uuid
from datetime import datetime

@app.route('/') # 路由
@app.route('/home')
def home():
    if current_user.is_authenticated:
        return render_template('home.html', user_id=current_user.user_ID)
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register(): # 註冊
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        name = request.form.get('name')
        password = request.form.get('password')
        
        # 檢查使用者是否存在
        if User.query.filter_by(user_ID=user_id).first():
            flash('使用者帳號已存在', 'error')
        
        try:
            # 建立新使用者
            newUser = User(user_ID=user_id, name=name, password=password)
            db.session.add(newUser)
            db.session.commit()
            flash('註冊成功！', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            User.session.rollback()
            flash('註冊失敗，請稍後再試', 'warning')
            return redirect(url_for('register'))
            
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login(): # 登入
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        password = request.form.get('password')
        
        # 檢查使用者是否存在
        user = User.query.filter_by(user_ID=user_id).first()
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('home', user_id=user_id))
        elif not user:
            flash('帳號或密碼錯誤', 'error')
        else:
            flash('帳號或密碼錯誤', 'error')
    
    return render_template('login.html')

@login_required
@app.route('/addNote', methods=['GET', 'POST'])
def addNote(): # 新增便利貼
    if request.method == 'POST':
        content = request.form.get('content')
        user_id = request.args.get('user_id')
        
        if not Note.user_ID  == user_id:
            # 建立新便利貼
            newNote = Note(note_ID=uuid.uuid4(), content=content, time=datetime.now(), user_id=user_id)
            Note.session.add(newNote)
            Note.session.commit()
            flash('新增便利貼成功！', 'success')
        else:
            # 更新便利貼
            updateNote = Note.query.filter_by(user_id=user_id).first()
            updateNote.content = content
            updateNote.time = datetime.now()
            Note.session.commit()
            flash('更新便利貼成功！', 'success')
        
        return redirect(url_for('home', user_id=user_id)) # 修改完重新導向至 home.html

    return render_template('addNote.html') # 回傳 addNote.html

@login_required
@app.route('/createRoom', methods=['GET', 'POST'])
def createRoom(): # 建立聊天室
    if request.method == 'POST':
        user_id1 = request.args.get('user_id1')
        user_id2 = request.args.get('user_id2')

        if Room.query.filter_by(user_id1=user_id1, user_id2=user_id2).first():
            flash('聊天室已存在！', 'error')
            return redirect(url_for('/room/<int:room_no>', room_no=Room.query.filter_by(user_id1=user_id1, user_id2=user_id2).first().room_no))
        elif Room.query.filter_by(user_id1=user_id2, user_id2=user_id1).first():
            flash('聊天室已存在！', 'error')
            return redirect(url_for('/room/<int:room_no>', room_no=Room.query.filter_by(user_id1=user_id2, user_id2=user_id1).first().room_no))
        else:
            # 建立新聊天室
            newRoom = Room(room_no=uuid.uuid4(), user_id1=user_id1, user_id2=user_id2)
            Room.session.add(newRoom)
            Room.session.commit()
            flash('建立聊天室成功！', 'success')
            return redirect(url_for('/room/<int:room_no>', room_no=newRoom.room_no))
    
    return render_template('createRoom.html')

@login_required
@app.route('/room/<int:room_no>', methods=['GET', 'POST'])
def chat(room_no): # 聊天室畫面
    return render_template('room.html', room_no=room_no)

@login_required
@app.route('/sendMessage', methods=['GET', 'POST'])
def sendMessage():
    pass