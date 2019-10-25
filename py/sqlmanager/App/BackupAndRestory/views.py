from flask import request,json
from . import BkAndRs
from App.BackupAndRestory.scheduler import *

@BkAndRs.route('/backup/',methods=["GET","POST"])
def back_up():
    '''点击提交后，执行备份、还原、创建用户等程序'''
    if request.method == "GET":
        message = {'code':1,'msg':'gun...'}
        return "<script>alert('Roll as far as you can')</script>"
    else:
        backup_list = request.json
        sche = Sche()
        data = sche.backup(backup_list)
        return json.dumps(data)

@BkAndRs.route('/restore/',methods=["GET","POST"])
def execute_sql():
    '''生成还原语句'''
    if request.method == "GET":
        message = {'code':1,'msg':'gun...'}
        return "<script>alert('Roll as far as you can')</script>"
    elif request.method == "POST":
        restore_list = request.json
        sche = Sche()
        data = sche.restore(restore_list)
        return json.dumps(data)

@BkAndRs.route('/getUsersql/',methods=['GET','POST'])
def userhandle():
    '''生成创建用户语句'''
    if request.method == "GET":
        pass
    elif request.method == "POST":
        userhandle_list = request.json
        print(userhandle_list)
        # sche = Sche()
        # data = sche.user(userhandle_list)
        return json.dumps('123')
    else:
        message = {'code':0,'msg':'未知的请求'}
        return json.dumps(message)

@BkAndRs.route('/exe_sql/',methods=["GET","POST"])
def exe_sql():
    '''执行修改后的sql语句'''
    if request.method == "GET":
        message = {'code':1,'msg':'gun...'}
        return "<script>alert('Roll as far as you can')</script>"
    else:
        request_list = request.json
        sche = Sche()
        data = sche.exe_sql(request_list)
        return json.dumps(data)