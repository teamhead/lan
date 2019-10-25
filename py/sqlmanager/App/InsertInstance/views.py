from flask import request,json
from . import IIstance
from App.InsertInstance.scheduler import *

@IIstance.route('/api/ins_instance/',methods=["POST","GET"])
def insert_instan():
    '''添加实例'''
    if request.method=="GET":
        pass
    else:
        datas = request.json
        print(datas)
        sche = Sche()
        message = sche.InsertInstance(datas)
        return json.dumps(message)


@IIstance.route('/api/queryInstance/',methods = ['POST','GET'])
def queryInstance():
    '''查询实例信息'''
    if request.method == "GET":
        return "ok"
    else:
        sche = Sche()
        message = sche.queryInstance()
        return json.dumps(message)

@IIstance.route('/api/queryInstanceAll/',methods = ["POST",'GET'])
def queryInstanceAll():
    ''''查询所有实例信息'''
    if request.method == "GET":
        pass
    if request.method == "POST":
        sche = Sche()
        message = sche.queryAllInstance()
        return json.dumps(message)

@IIstance.route('/api/updateInstance/',methods = ['POST','GET'])
def updateInstance():
    '''修改实例信息'''
    if request.method == "GET":
        pass
    elif request.method == "POST":
        instanceInfo_list = request.json
        sche = Sche()
        message = sche.updateInstance(instanceInfo_list)
        return json.dumps(message)

@IIstance.route('/api/deleteInstance/',methods = ['POST','GET'])
def deleteInstance():
    '''禁用实例信息'''
    if request.method == 'GET':
        pass
    elif request.method == "POST":
        data = request.json
        sche = Sche()
        message = sche.deleteInstance(data)
        return json.dumps(message)



# @IIstance.route('/ins_db/',methods=["POST"])
# def ins_db():
#     '''同步数据库名'''
#     if request.method == "GET":
#         result = {'status': '添加成功'}
#         return json.dumps(result)
#     elif request.method == "POST":
#         data = request.json
#         host = 'rm-wz9954fkn5h96zerz.mysql.rds.aliyuncs.com'
#         user = 'db_mng_user'
#         passwd = 'X2rePFHQaY-mGEdFcCM9n'
#         port = 3306
#         if data:
#             print(data)
#             for dat in data:
#                 if dat['name'] == "easname":
#                     easname = dat['value']
#                     BKARS = BackupAndRestore(host=host, user=user, passwd=passwd, port=port)
#                     new_process = Process(target=BKARS.update_db_info,args=(easname,))
#                     new_process.start()
#                     result = {'status':'同步已提交'}
#                     return json.dumps(result)
#                 else:
#                     result = {'status':'请输入正确的实例名'}
#                     return json.dumps(result)
#         result = {'status':'添加成功'}
#         return json.dumps(result)

