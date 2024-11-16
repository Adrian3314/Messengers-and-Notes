from flask import Flask, render_template, request, redirect, url_for
from app import app

@app.route('/') # 路由
@app.route('/home')
def home():
    return render_template('home.html') # 回傳 home.html
