from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote
import cloudinary
from flask_login import LoginManager
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:%s@localhost/saledb?charset=utf8mb4" % quote("Admin@123")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.secret_key='1978324yhdfjg183ysdfzxc??>m.bvk'
app.config["PAGE_SIZE"] = 8

db = SQLAlchemy(app)

cloudinary.config(cloud_name='12adfgertjhe5',
                  api_key='',
                  api_secret='')

login = LoginManager(app)
