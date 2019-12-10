import datetime

from dbconnection import db

class ExamRecord(db.Model):
    __tablename__ = 'ExamRecord'
    examRecordID=db.Column(db.Integer,primary_key = True, autoincrement = True,nullable=False)
    questionsBankID=db.Column(db.Integer)
    username=db.Column(db.String(255))
    score=db.Column(db.String(255))
    submitTime=db.Column(db.String(255))




def c_examrecord(qid,un):
    query_exid=ExamRecord.query.all()

    time=datetime.datetime.strftime(datetime.datetime.now(),'%Y-%m-%d %H:%M:%S')
    new_ExamRecord= ExamRecord(examRecordID=len(query_exid),questionsBankID=qid,username=un,score="0",submitTime=time)
    db.session.add(new_ExamRecord)
    db.session.commit()
    return len(query_exid)

