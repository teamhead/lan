from flask import request,json
from App.InsertDb.scheduler import *
from . import QItance

@QItance.route('/queryDb/',methods=["GET","POST"])
def queryDb():
    '''查询已同步数据库信息'''
    if request.method == "GET":
        pass
    elif request.method=="POST":
        instanceInfo = request.json
        sche = Sche()
        data = sche.queryDB(instanceInfo)
        return json.dumps(data)

@QItance.route('/insertDBInfo/',methods=["POST","GET"])
def insertDBInfo():
    '''添加数据库名至mysql'''
    if request.method == "GET":
        pass
    elif request.method == "POST":
        instanceInfo = request.json
        sche = Sche()
        message = sche.insert_Db(instanceInfo)
        return json.dumps(message)


@QItance.route('/updateDB/',methods = ["POST","GET"])
def updateDB():
    if request.method == "GET":
        pass
    elif request.method == "POST":
        pass


@QItance.route("/deleteDB/",methods = ["POST","GET"])
def deleteDB():
    if request.method == "GET":
        pass
    elif request.method == "POST":
        pass



@QItance.route('/select_db/',methods=["GET","POST"])
def query_db():
    '''根据实例信息获取相应的数据库信息'''
    if request.method=="POST":
        name = request.json
        Dbmysql = Data_mysql('rm-wz9954fkn5h96zerz.mysql.rds.aliyuncs.com', 'db_mng_user', 'X2rePFHQaY-mGEdFcCM9n','db_manage_pfm', 3306)
        mysql = "select db_name from instance_info a inner join db_info b on a.instance_id=b.instance_id where a.isvalid=1 and b.isvalid=1 and a.instance_name='%s'"%name['name']
        datas = Dbmysql.select_mysql_Db(mysql)
        db_name_list=[]
        if datas:
            for data in datas:
                db_name_list.append(data[0])
        return json.dumps(db_name_list)
