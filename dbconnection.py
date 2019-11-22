from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import pymysql


acc = Flask(__name__)


acc.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:bf746b14ef5cc35a@122.51.255.112:3306/examination_system"

#配置flask配置对象中键：SQLALCHEMY_COMMIT_TEARDOWN,设置为True,应用会自动在每次请求结束后提交数据库中变动

acc.config['SQLALCHEMY_COMMIT_TEARDOWN'] = True
acc.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


db = SQLAlchemy(acc)