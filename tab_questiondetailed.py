from dbconnection import db

class QuestionDetailed(db.Model):
    __tablename__ = 'QuestionDetailed'
    questionDetailedID=db.Column(db.Integer,primary_key = True, autoincrement = True,nullable=False)
    questionsID=db.Column(db.Integer)
    questionsBankID=db.Column(db.String)
def get_questionids(qb_id):
    qid_bank_0 = QuestionDetailed.query.filter(QuestionDetailed.questionsBankID == qb_id).all()
    list = []

    for i in qid_bank_0:
        list.append(i.questionsID)
    print(list)


    return {
        "qid_bank":list
    }
