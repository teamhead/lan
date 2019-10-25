from flask import request,json
from multiprocessing import Process
from App.BackupAndRestory.backupAndRestore import *
from . import IIstance



@IIstance.route('/ins_instance/',methods=["POST","GET"])
def insert_instan():
    '''添加实例'''
    if request.method=="GET":
        pass
    else:
        datas = request.json
        if datas:
            for data in datas:
                if data['name'] == 'easname':
                    easname = data['value']
                elif data['name'] == "ipaddr":
                    ipaddr = data['value']
                elif data['name'] == 'db_port':
                    db_port = data['value']
                elif data['name'] == 'username':
                    username = data['value']
                elif data['name'] == 'passwd':
                    passwd = data['value']
            Dbmysql = Data_mysql('127.0.0.1', 'db_mng_user', 'X2rePFHQaY-mGEdFcCM9n','db_manage_pfm', 3306)
            mysql = "insert into instance_info(instance_name,instance_ip_addr,instance_db_port,instance_user_name,instance_passwd) values('{0}','{1}','{2}','{3}','{4}')".format(easname,ipaddr,db_port,username,passwd)
            datas = Dbmysql.insert_mysql_Db(mysql)
            result = {'status':'添加成功'}
            return json.dumps(result)
        else:
            data_file = {'status':'缺少关键字'}
            return json.dumps((data_file))

@IIstance.route('/ins_db/',methods=["POST"])
def ins_db():
    '''同步数据库名'''
    if request.method == "GET":
        result = {'status': '添加成功'}
        return json.dumps(result)
    elif request.method == "POST":
        data = request.json
        host = '127.0.0.1'
        user = 'db_mng_user'
        passwd = 'X2rePFHQaY-mGEdFcCM9n'
        port = 3306
        if data:
            print(data)
            for dat in data:
                if dat['name'] == "easname":
                    easname = dat['value']
                    BKARS = BackupAndRestore(host=host, user=user, passwd=passwd, port=port)
                    new_process = Process(target=BKARS.update_db_info,args=(easname,))
                    new_process.start()
                    result = {'status':'同步已提交'}
                    return json.dumps(result)
                else:
                    result = {'status':'请输入正确的实例名'}
                    return json.dumps(result)
        result = {'status':'添加成功'}
        return json.dumps(result)

