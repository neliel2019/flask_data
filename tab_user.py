from dbconnection import db

class User(db.Model):

    username=db.Column(db.String(255),primary_key=True)
    passwrod=db.Column(db.String(255),primary_key=True)


def getpassword():
    u1=User.query.filter(User.username=="aaaa").all()
    return u1