from dbconnection import db
import json

class QuestionBank(db.Model):
    __tablename__ = 'QuestionBank'
    questionsBankID=db.Column(db.Integer,primary_key=True,autoincrement=True)
    questionsBankName=db.Column(db.String(255))
    creatTime=db.Column(db.String(255))

    def __init__(self, questionsBankID, questionsBankName,creatTime):
        self.questionsBankID = questionsBankID
        self.questionsBankName = questionsBankName
        self.creatTime=creatTime

def getQuestionBankID(qbname):
    bank = QuestionBank.query.filter(QuestionBank.questionsBankName == qbname).first()

    return bank.questionsBankID






def getQuestionName():

    bank = QuestionBank.query.all();
    list=[]
    a=0
    for i in bank:

        ap={"questionsBankID":i.questionsBankID,"questionsBankName" : i.questionsBankName,"creatTime":i.creatTime}
        list.append(ap)
        a += 1







    return list;


