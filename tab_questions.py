from dbconnection import db

class Questions(db.Model):

    questionsID=db.Column(db.Integer,primary_key=True,autoincrement=True)
    questionsTitle=db.Column(db.String(255))
    courseID=db.Column(db.Integer)
    topicID=db.Column(db.Integer)
    rightOption=db.Column(db.String(255))
    optionA=db.Column(db.String(255))
    optionB=db.Column(db.String(255))
    optionC=db.Column(db.String(255))
    optionD=db.Column(db.String(255))
    questionScore=db.Column(db.String(255))
    questionsType=db.Column(db.Integer)





    def __init__(self, questionsID, questionsTitle,courseID,topicID,rightOption,optionA,optionB,optionC,optionD,questionScore,questionsType):
        self.questionsID = questionsID
        self.questionsTitle = questionsTitle
        self.courseID=courseID
        self.topicID = topicID
        self.rightOption = rightOption
        self.optionA = optionA
        self.optionB = optionB
        self.optionC = optionC
        self.optionD = optionD
        self.questionScore = questionScore
        self.questionsType = questionsType


    def __repr__(self):

        return ""

    def getquestion(q_id):
        question = Questions.query.filter(Questions.questionsID ==q_id).first()
        return {
            "questionsID":question.questionsID,
            "questionsTitle":question.questionsTitle,
            "courseID":question.courseID,
            "topicID": question.topicID,
            "rightOption": question.rightOption,
            "optionA": question.optionA,
            "optionB": question.optionB,
            "optionC": question.optionC,
            "optionD": question.optionD,
            "questionScore": question.questionScore,
            "questionsType": question.questionsType,

        }


