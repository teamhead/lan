from flask import request,json
from App.BackupAndRestory.backupAndRestore import *
from multiprocessing import Process
from . import BkAndRs

@BkAndRs.route('/backup/',methods=["GET","POST"])
def back_up():
    '''点击提交后，执行备份、还原、创建用户等程序'''
    if request.method == "GET":
        return 'alsdkfjhlsadjflsdjflksadjflksadjflksda'
    else:
        backup_list = request.json
        print(backup_list)
        if backup_list:
            for back_up in backup_list:
                if back_up['name']=='instance_name':
                    instance_name=back_up['value']
                elif back_up['name']=='OperType':
                    OperType = back_up['value']
                elif back_up['name'] == "instance_name_store":
                    instance_name_store = back_up['value']
            if OperType == '还原' or OperType == '创建账户':
                mysql = "select instance_ip_addr,instance_db_port,instance_user_name,instance_passwd from instance_info where instance_name='{0}'".format(instance_name_store)
                Dbmysql = Data_mysql('127.0.0.1', 'db_mng_user', 'X2rePFHQaY-mGEdFcCM9n','db_manage_pfm', 3306)
                datas = Dbmysql.select_mysql_Db(mysql)
            elif OperType == '备份':
                mysql = "select instance_ip_addr,instance_db_port,instance_user_name,instance_passwd from instance_info where instance_name='{0}'".format(instance_name)
                Dbmysql = Data_mysql('127.0.0.1', 'db_mng_user', 'X2rePFHQaY-mGEdFcCM9n','db_manage_pfm', 3306)
                datas = Dbmysql.select_mysql_Db(mysql)
            else:
                print(OperType)
        if datas:
            host = datas[0][0]
            port = datas[0][1]
            user = datas[0][2]
            passwd = datas[0][3]
            BKARS = BackupAndRestore(host= host, user= user, passwd=passwd, port=port, backup_list=backup_list)
            if OperType == '备份':
                backup_process = Process(target=BKARS.backup,args=())
                backup_process.start()
                return '已提交备份'
            elif OperType == '还原':
                restore_process = Process(target=BKARS.restore,args=())
                restore_process.start()
                return '已提交备份'
            elif OperType == '创建账户':
                createuser_process = Process(target=BKARS.restore,args=())
                createuser_process.start()
                return '已提交备份'


@BkAndRs.route('/exe_sql/',methods=["GET","POST"])
def execute_sql():
    if request.method == "GET":
        pass
    elif request.method == "POST":
        restore_list = request.json
        if restore_list:
            for back_up in restore_list:
                if back_up['name']=='instance_name':
                    instance_name=back_up['value']
                elif back_up['name']=='OperType':
                    OperType = back_up['value']
                elif back_up['name'] == "instance_name_store":
                    instance_name_store = back_up['value']
            try:
                if instance_name_store:
                    mysql = "select instance_ip_addr,instance_db_port,instance_user_name,instance_passwd from instance_info where instance_name='{0}'".format(instance_name)
                else:
                    mysql = "select instance_ip_addr,instance_db_port,instance_user_name,instance_passwd from instance_info where instance_name='{0}'".format(instance_name_store)
                Dbmysql = Data_mysql('127.0.0.1', 'db_mng_user', 'X2rePFHQaY-mGEdFcCM9n','db_manage_pfm', 3306)
                datas = Dbmysql.select_mysql_Db(mysql)
                if datas:
                    host = datas[0][0]
                    port = datas[0][1]
                    user = datas[0][2]
                    passwd = datas[0][3]
                    BKARS = BackupAndRestore(host=host, user=user, passwd=passwd, port=port, backup_list=restore_list)
                    message_sql = BKARS.get_sql()
                    if message_sql == "":
                        message_sql = '此用户没有执行备份或还原'
                        return json.dumps(message_sql)
                    else:
                        return json.dumps(message_sql)
                else:
                    massage_sql = "无此实例信息，请核对输入选项"
                    return json.dumps(massage_sql)
            except FloatingPointError:
                message_sql = '请核对输入选项'
                return json.dumps(message_sql)
        else:
            massage_sql = '数据传输失败'
            return json.dumps(massage_sql)
