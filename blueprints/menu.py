from flask import Blueprint
from flask import Flask,request,render_template,session,redirect,url_for,jsonify
from sqlalchemy import text
from exts import db
import hashlib
import json
# from models.table import User, Admin
import os
import time

bp = Blueprint('menu',__name__,url_prefix="/")

@bp.route('/menu', methods = ['GET','POST'])
def menu():
    sql = text('SELECT * FROM DormInfo')
    r = db.session.execute(sql).fetchall()
    # print(r)
    # for a in results:
    #     print(a.InfoID)

    return render_template('menu.html', results = r)

@bp.route('/add_action', methods = ['GET','POST'])
def add_action():
    data = request.get_json()
    id = data.get('id')
    name = data.get('name')
    attribute1 = data.get('attribute1')
    attribute2 = data.get('attribute2')
    attribute3 = data.get('attribute3')
    attribute4 = data.get('attribute4')

    # {id: id,name: name, attribute1: attribute1, attribute2: attribute2, attribute3: attribute3, attribute4: attribute4}
    sql = text('insert into DormInfo value(:id, :name, :attribute1, :attribute2, :attribute3, :attribute4)')
    db.session.execute(sql,{'id': id,'name': name, 'attribute1': attribute1, 'attribute2': attribute2, 'attribute3': attribute3, 'attribute4': attribute4})
    db.session.commit()

    status = 'success'
    return jsonify({'status':status})
