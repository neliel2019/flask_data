from dbconnection import db

class User(db.Model):
    __tablename__ = 'User'
    username=db.Column(db.String(255),primary_key=True)
    passwrod=db.Column(db.String(255))
    authority=db.Column(db.String(255))

    def __init__(self, username, passwrod,authority):
        self.username = username
        self.passwrod = passwrod
        self.authority=authority

    def __repr__(self):
        return '<User %r>' % self.username


def login_cheek(usernameByWeb,pswByWeb):
    u1=User.query.filter(User.username==usernameByWeb).first()

    if u1==None:
        return 0

    elif(usernameByWeb==u1.username and pswByWeb==u1.passwrod):

      return 1
    else:
        return 0
def register_user(r_username,r_password):
    u2=User.query.filter(User.username==r_username).first()
    if (u2 == None):
        new_user = User(r_username, r_password, '1')
        db.session.add(new_user)
        db.session.commit()
        return 1
    else:

        return 0








