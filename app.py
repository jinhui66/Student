from flask import Flask, render_template, session, redirect, Blueprint, request, jsonify
import hashlib
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from sqlalchemy import text
import config
from blueprints.login import bp as login_bp
from blueprints.menu import bp as menu_bp
from exts import db

app = Flask(__name__)

app.config.from_object(config)

db.init_app(app)

app.register_blueprint(login_bp)
app.register_blueprint(menu_bp)


if __name__ == '__main__':
    app.run(debug=True)
