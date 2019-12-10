from flask import Flask, json
from tab_user import login_cheek
from tab_user import register_user
from tab_questionsbank import getQuestionName
from serialization import set_default
from tab_exam_record import c_examrecord
from tab_questiondetailed import get_questionids


from dbconnection import acc

from flask import request


@acc.route('/api/login',methods=['POST','GET'])
def login_web():
    ac=request.get_data()
    json_data=json.loads(ac.decode("utf-8"))
    username=str(json_data.get("username"))
    password = str(json_data.get("password"))

    print(username,password)
    check_code=login_cheek(username,password)
    if(check_code==1):
        return {
            "login_check_code":check_code,
            "login_message":"登录成功！"
        }
    else:
        return {
            "login_check_code": check_code,
            "login_message": "登录失败！"
        }

@acc.route('/api/register',methods=['POST','GET'])
def register_web():#提供登录验证
    register_web_request_data = request.get_data()
    register_web_json= json.loads(register_web_request_data.decode("utf-8"))
    r_username = str(register_web_json.get("r_username"))
    r_password = str(register_web_json.get("r_password"))
    print(r_username,r_password)
    register_code=register_user(r_username,r_password)
    if(register_code==1):
        return {
            "register_code":register_code,
            "register_message":"注册成功"
        }
    else:
        return {
            "register_code": 0,
            "register_message": "该用户名已被使用"
        }

@acc.route('/api/getQuestionName',methods=['POST','GET'])

def m_getQuestionName():#提供试卷名
    print(getQuestionName())
    list=getQuestionName()

    data={
        "questionsbanks":list,
    }
    data1=json.dumps(data, ensure_ascii=False)
    print(data1)

    return data1

@acc.route('/api/setExamRecord',methods=['POST','GET'])
def m_setExamRecord():
    register_web_request_data = request.get_data()
    register_web_json = json.loads(register_web_request_data.decode("utf-8"))
    s_questionsbanksid = str(register_web_json.get("b_questionsbanksid"))
    s_username = str(register_web_json.get("b_username"))
    print(s_questionsbanksid,s_username)
    a=c_examrecord(s_questionsbanksid,s_username)
    print(a)

    return {
        "setExamRecordmessage":"1"
    }
@acc.route('/api/getQuestion',methods=['POST','GET'])
def m_getQuestion():
    web_request_data = request.get_data()
    web_json = json.loads(web_request_data.decode("utf-8"))
    s_question_id_bank = str(web_json.get("questionBankID"))


    return get_questionids(s_question_id_bank)










if __name__ == '__main__':
    acc.run()

