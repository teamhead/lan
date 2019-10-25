from flask import request,json
from App.Model.model import *
from . import QItance

@QItance.route('/select_instance/',methods=["GET","POST"])
def query_instance():
    '''查询所有实例信息'''
    if request.method=="GET":
        Dbmysql = Data_mysql('127.0.0.1', 'db_mng_user', 'X2rePFHQaY-mGEdFcCM9n','db_manage_pfm', 3306)
        mysql = "select instance_name from instance_info"
        datas = Dbmysql.select_mysql_Db(mysql)
        instance_name_dict={}
        if datas:
            i = 1
            for data in datas:
                instance_name_dict['instance_name_'+str(i)]=data[0]
                i+=1
        return json.dumps(instance_name_dict)

@QItance.route('/select_db/',methods=["GET","POST"])
def query_db():
    '''根据实例信息获取相应的数据库信息'''
    if request.method=="POST":
        name = request.json
        Dbmysql = Data_mysql('127.0.0.1', 'db_mng_user', 'X2rePFHQaY-mGEdFcCM9n','db_manage_pfm', 3306)
        mysql = "select db_name from instance_info a inner join db_info b on a.instance_id=b.instance_id where a.isvalid=1 and b.isvalid=1 and a.instance_name='%s'"%name
        datas = Dbmysql.select_mysql_Db(mysql)
        db_name_list=[]
        if datas:
            for data in datas:
                db_name_list.append(data[0])
        return json.dumps(db_name_list)
