from flask import Flask, render_template, request, redirect, url_for, flash
from models import User, Note, Message, Room
from app import app
import uuid
from datetime import datetime

@app.route('/') # 路由
@app.route('/home')
def home():
    return render_template('home.html') # 回傳 home.html

@app.route('/register', methods=['GET', 'POST']) # 路由
def register():
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        name = request.form.get('name')
        password = request.form.get('password')
        
        # 檢查使用者是否存在
        if User.query.filter_by(user_id=user_id).first():
            flash('使用者帳號已存在')
        
        try:
            # 建立新使用者
            newUser = User(user_id=user_id, name=name, password=password)
            User.session.add(newUser)
            User.session.commit()
            flash('註冊成功！')
            return redirect(url_for('login'))
        except Exception as e:
            User.session.rollback()
            flash('註冊失敗，請稍後再試')
            return redirect(url_for('register'))
            
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        password = request.form.get('password')
        
        # 檢查使用者是否存在
        user = User.query.filter_by(user_id=user_id).first()
        if user and user.password == password:
            return redirect(url_for('home', user_id=user_id))
        else:
            flash('帳號或密碼錯誤')
            return redirect(url_for('login'))
    
    return render_template('login.html')

@app.route('/addNote', methods=['GET', 'POST'])
def addNote():
    if request.method == 'POST':
        content = request.form.get('content')
        user_id = request.args.get('user_id')
        
        if not Note.user_ID  == user_id:
            # 建立新筆記
            newNote = Note(note_ID=uuid.uuid4(), content=content, time=datetime.now(), user_id=user_id)
            Note.session.add(newNote)
            Note.session.commit()
            flash('新增筆記成功！')
        else:
            # 更新筆記
            updateNote = Note.query.filter_by(user_id=user_id).first()
            updateNote.content = content
            updateNote.time = datetime.now()
            Note.session.commit()
            flash('更新筆記成功！')
        
        return redirect(url_for('home', user_id=user_id))

    return render_template('addNote.html')