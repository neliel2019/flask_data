from flask import Flask, json
from tab_user import login_cheek
from tab_user import register_user
from tab_questionsbank import getQuestionName

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
def register_web():
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

def m_getQuestionName():

    print(getQuestionName())

    return "oo"










if __name__ == '__main__':
    acc.run()

