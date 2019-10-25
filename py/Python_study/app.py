'''
作者：兰嘉轩
创建时间: 2019年8月19日
描述: 数据库管理系统
'''


from flask import request,Flask
import json
from flask_cors import *
from multiprocessing import Process
from BackupAndRestory.backupAndRestore import *
from zabbix.zabbix_handle import *
from zabbix.zabbix_aut_find import *

app = Flask(__name__)
# 引入配置文件
app.config.from_pyfile('config.py')
# 解决flask跨域问题
CORS(app, supports_credentials=True)

@app.route('/select_instance/',methods=["GET","POST"])
def query_instance():
    '''查询所有实例信息'''
    if request.method=="GET":
        Dbmysql = Data_mysql('rm-wz9954fkn5h96zerz.mysql.rds.aliyuncs.com', 'db_mng_user', 'X2rePFHQaY-mGEdFcCM9n','db_manage_pfm', 3306)
        mysql = "select instance_name from instance_info"
        datas = Dbmysql.select_mysql_Db(mysql)
        instance_name_dict={}
        if datas:
            i = 1
            for data in datas:
                instance_name_dict['instance_name_'+str(i)]=data[0]
                i+=1
        return json.dumps(instance_name_dict)


@app.route('/select_db/',methods=["GET","POST"])
def query_db():
    '''根据实例信息获取相应的数据库信息'''
    if request.method=="POST":
        name = request.json
        Dbmysql = Data_mysql('rm-wz9954fkn5h96zerz.mysql.rds.aliyuncs.com', 'db_mng_user', 'X2rePFHQaY-mGEdFcCM9n','db_manage_pfm', 3306)
        mysql = "select db_name from instance_info a inner join db_info b on a.instance_id=b.instance_id where a.isvalid=1 and b.isvalid=1 and a.instance_name='%s'"%name
        datas = Dbmysql.select_mysql_Db(mysql)
        db_name_list=[]
        if datas:
            for data in datas:
                db_name_list.append(data[0])
        return json.dumps(db_name_list)


@app.route('/backup/',methods=["GET","POST"])
def back_up():
    '''点击提交后，执行备份、还原、创建用户等程序'''
    if request.method == "GET":
        pass
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
                Dbmysql = Data_mysql('rm-wz9954fkn5h96zerz.mysql.rds.aliyuncs.com', 'db_mng_user', 'X2rePFHQaY-mGEdFcCM9n','db_manage_pfm', 3306)
                datas = Dbmysql.select_mysql_Db(mysql)
            elif OperType == '备份':
                mysql = "select instance_ip_addr,instance_db_port,instance_user_name,instance_passwd from instance_info where instance_name='{0}'".format(instance_name)
                Dbmysql = Data_mysql('rm-wz9954fkn5h96zerz.mysql.rds.aliyuncs.com', 'db_mng_user', 'X2rePFHQaY-mGEdFcCM9n','db_manage_pfm', 3306)
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

@app.route('/ins_instance/',methods=["POST","GET"])
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
            Dbmysql = Data_mysql('rm-wz9954fkn5h96zerz.mysql.rds.aliyuncs.com', 'db_mng_user', 'X2rePFHQaY-mGEdFcCM9n','db_manage_pfm', 3306)
            mysql = "insert into instance_info(instance_name,instance_ip_addr,instance_db_port,instance_user_name,instance_passwd) values('{0}','{1}','{2}','{3}','{4}')".format(easname,ipaddr,db_port,username,passwd)
            datas = Dbmysql.insert_mysql_Db(mysql)
            result = {'status':'添加成功'}
            return json.dumps(result)
        else:
            data_file = {'status':'缺少关键字'}
            return json.dumps((data_file))


@app.route('/ins_db/',methods=["POST"])
def ins_db():
    '''同步数据库名'''
    if request.method == "GET":
        result = {'status': '添加成功'}
        return json.dumps(result)
    elif request.method == "POST":
        data = request.json
        host = 'rm-wz9954fkn5h96zerz.mysql.rds.aliyuncs.com'
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

@app.route('/exe_sql/',methods=["GET","POST"])
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
                Dbmysql = Data_mysql('rm-wz9954fkn5h96zerz.mysql.rds.aliyuncs.com', 'db_mng_user', 'X2rePFHQaY-mGEdFcCM9n','db_manage_pfm', 3306)
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

# 添加监控信息
@app.route('/ins_zabbix/',methods=["GET","POST"])
def ins_zabbix():
    '''自动发现页添加数据'''
    if request.method == "GET":
        pass
    elif request.method == "POST":
        zabbix_list = request.json
        print(zabbix_list)
        zbx = Zabbix(zabbix_list)
        message = zbx.add()
        second = '*/1'
        exe = Exec_func(second)
        exe.exe_fun()
        return json.dumps(message)

# 查询监控信息
@app.route('/query_data/',methods=["GET","POST"])
def query_data():
    '''自动发现页查询数据信息'''
    if request.method=="GET":
        pass
    elif request.method == "POST":
        zabbix_list = request.json
        zbx = Zabbix(zabbix_list)
        results = zbx.query()
        return json.dumps(results)



# 调用接口，生成发现监控项json字符串
@app.route('/sql_api/',methods=["POST","GET"])
def sql_api():
    if request.method=="GET":
        print()
    elif request.method=="POST":
        datas = request.json
        print(datas)
        if datas:
            for data in datas:
                pass
        zbx = Zabbix()
        result = zbx.parse_str(data)
        return json.dumps(result)
def print_l():
    print("我是定时任务")


if __name__ == '__main__':
    app.run()
