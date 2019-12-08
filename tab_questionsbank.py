from dbconnection import db

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
