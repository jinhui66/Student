from flask import Blueprint
from flask import Flask,request,render_template,session,redirect,url_for,jsonify
from sqlalchemy import text
from exts import db
import hashlib
import json
# from models.table import User, Admin
import os
import time

bp = Blueprint('login',__name__,url_prefix="/")

@bp.route('/', methods=['GET', 'POST'])
def index():
    return redirect('login')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@bp.route('/login_action', methods=['GET', 'POST'])
def login_action():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # connection = get_db_connection()
    sql = text("SELECT * FROM Stu WHERE SAccount = :username AND SPasswd = :password")
    result = db.session.execute(sql, {'username': username, 'password': password}).fetchone()

    if result is not None:
        # 登录成功
        return jsonify(success=True)
    else:
        # 登录失败
        return jsonify(success=False)
