from flask import Flask
from tab_user import getpassword

from dbconnection import acc


@acc.route('/')
def hello_world():
    print(getpassword())
    return 'Hello World!'


if __name__ == '__main__':
    acc.run()

