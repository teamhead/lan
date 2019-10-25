from App.Model.Mysql import *

class Zabbix(object):
    def __init__(self,zabbix_list=[]):
        self.host = 'rm-wz9954fkn5h96zerz.mysql.rds.aliyuncs.com'
        self.port = 3306
        self.passwd = 'X2rePFHQaY-mGEdFcCM9n'
        self.user = 'db_mng_user'
        self.db =  'db_manage_pfm'
        self.exmysql = Data_mysql(self.host, self.user, self.passwd, self.db, self.port)
        self.results = {}
        self.result_parse =[]
        self.results['data'] = []
        self.zabbix_list = zabbix_list
        if self.zabbix_list:
            for zabbix_info in self.zabbix_list:
                if zabbix_info['name']=='key':
                    self.key = zabbix_info['value']
                elif zabbix_info['name']=="ins_key":
                    self.ins_key = zabbix_info['value']
                elif zabbix_info['name'] == 'db_name':
                    self.db_name = zabbix_info['value']
                elif zabbix_info['name'] == 'ins_db_name':
                    self.ins_db_name = zabbix_info['value']
                elif zabbix_info['name'] == 'ins_sql_message':
                    self.ins_sql_message = zabbix_info['value']
                elif zabbix_info['name'] =='ins_description':
                    self.ins_description = zabbix_info['value']
                elif zabbix_info['name'] == "queryTime":
                    if zabbix_info['value']:
                        self.queryTime = int(zabbix_info['value'])
                    else:
                        self.queryTime = ''
                elif zabbix_info['name'] == "ins_queryTime":
                    self.ins_queryTime = zabbix_info['value']
                elif zabbix_info['name'] == 'ins_type':
                    self.ins_type = zabbix_info['value']
        else:
            print('没有输入数据')
        self.key_list = []
        self.sql_content_list = []
        self.mon_interval_list = []
        self.type_list = []
        self.db_id_list = []
        self.description_list = []

    # db_id转换为db_name
    def db_id_switch_name(self,db_id):
        mysql = "select db_name from db_info where db_id='{0}'".format(db_id)
        db_name = self.exmysql.select_mysql_Db(mysql)[0][0]
        return db_name
    # db_name转换为db_id
    def db_name_switch_id(self,db_name):
        mysql = "select db_id from db_info where db_name='{0}'".format(db_name)
        db_id = self.exmysql.select_mysql_Db(mysql)[0][0]
        return db_id

    # 拼接返回结果
    def parseStr(self,datas):
        for data in datas:
            result = {'key': data[0], 'db_name': self.db_id_switch_name(data[4]), 'sql_message': data[1],
                      'type': data[3], 'mon_interval': data[2], 'description': data[5]}
            self.result_parse.append(result)
        return self.result_parse

    # 判断输入的数据
    def query(self):
        if self.zabbix_list:
            if self.key != '':
                Mysql = "select monitorkey,sql_content,mon_interval,type,db_id,description from zabbix_monitor_config where monitorkey='{0}'".format(
                    self.key)
                datas = self.exmysql.select_mysql_Db(Mysql)
                results = self.parseStr(datas)
                return results
            elif self.db_name != '':
                Mysql = "select monitorkey,sql_content,mon_interval,type,db_id,description from zabbix_monitor_config where db_id='{0}'".format(
                    self.db_name_switch_id(self.db_name))
                datas = self.exmysql.select_mysql_Db(Mysql)
                results = self.parseStr(datas)
                return results
            elif self.queryTime != '':
                Mysql = "select monitorkey,sql_content,mon_interval,type,db_id,description from zabbix_monitor_config where mon_interval='{0}'".format(
                    self.queryTime)
                datas = self.exmysql.select_mysql_Db(Mysql)
                results = self.parseStr(datas)
                return results
            elif self.db_name != '' and self.queryTime != '':
                Mysql = "select monitorkey,sql_content,mon_interval,type,db_id,description from zabbix_monitor_config where mon_interval='{0}' and db_id='{1}'".format(
                    self.queryTime,self.db_name_switch_id(self.db_name))
                datas = self.exmysql.select_mysql_Db(Mysql)
                results = self.parseStr(datas)
                return results
            elif self.key == '' and self.db_name == '' and self.queryTime == '':
                Mysql = "select monitorkey,sql_content,mon_interval,type,db_id,description from zabbix_monitor_config"
                datas = self.exmysql.select_mysql_Db(Mysql)
                print(datas)
                results = self.parseStr(datas)
                return results
            else:
                results = []
                return results
        else:
            pass
    # 添加监控信息
    def add(self):
        if self.zabbix_list:
            if self.ins_key and self.ins_sql_message and self.ins_queryTime and self.ins_type and self.ins_db_name and self.ins_description:
                mysql = '''insert into zabbix_monitor_config(monitorkey,sql_content,mon_interval,type,db_id,description) values ("{0}","{1}","{2}","{3}","{4}","{5}")'''.format(
                    self.ins_key,
                    self.ins_sql_message,
                    self.ins_queryTime,
                    self.ins_type,
                    self.db_name_switch_id(self.ins_db_name),
                    self.ins_description
                )
                print(mysql)
                self.exmysql.insert_mysql_Db(mysql)
                message={'code':0,"message":'添加成功'}
                return message
        else:
            message = {'code': 0, "message": '没有数据输入'}
            return message

    # 更新监控信息
    def update(self):
        pass
    # 删除监控信息
    def delete(self):
        pass

    # 解析字符串
    def parse_str(self,result):
        # 根据拿到的分类信息获取，获取zabbix_monitor_config所有的数据列表
        sql = "select monitorkey,sql_content,mon_interval,type,db_id,description from zabbix_monitor_config where type='{0}'".format(result)
        print(sql)
        datas = self.exmysql.insert_mysql_Db(sql)
        # print(datas)
        if datas:
            for message in datas:
                self.key = message[0]
                self.sql_content = message[1]
                self.mon_interval= message[2]
                self.type = message[3]
                self.description = message[5]
                print(self.key)
                print(self.sql_content)
                print(self.mon_interval)
                print(self.type)
                print(self.description)

                # 拼接字符串
                if result == "str":
                    print(self.key,self.description)
                    self.results['data'].append({"{#SQLINT}": self.key,"{#description}":self.description})
                elif result == 'int':
                    print(self.key, self.description)
                    self.results['data'].append({"{#SQLINT}": self.key,"{#description}":self.description})
        return self.results

    def zabbix_sender(self, result):
        sql = "select monitorkey,sql_content,mon_interval,type,db_id,description from zabbix_monitor_config where type='{0}'".format(result)
        datas = self.exmysql.insert_mysql_Db(sql)
        # print(datas)
        if datas:
            for message in datas:
                self.key = message[0]
                self.sql_content = message[1]
                self.mon_interval= message[2]
                self.type = message[3]
                self.description = message[5]
                print(self.key)
                print(self.sql_content)
                print(self.mon_interval)
                print(self.type)
                print(self.description)
    def parse_sender(self,host,username,password,database,port,type):
        query_sql = Data_mysql(host,username,password,database,port)
        exec_sql = "select sql_content,db_id from zabbix_monitor_config where type='{0}'".format(type)
        # 按照类型查询监控项
        datas = query_sql.select_mysql_Db(query_sql)
        if datas:
            for data in datas:
                instance_sql = data[0][0]
                db_id = data[0][1]
                sql = "select b.instance_ip_addr,b.instance_db_port,b.instance_user_name,b.instance_passwd from db_info as a inner join instance_info as b on a.instance_id=b.instance_id and a.db_id={0}".format(db_id)

                sqlserver_info = query_sql.select_mysql_Db(sql)
                if sqlserver_info:
                    host = sqlserver_info[0][0]
                    port = sqlserver_info[0][1]
                    user = sqlserver_info[0][2]
                    passwd = sqlserver_info[0][3]
                    database = "E6ManageDB"
                    sqlserver = Data_SQLserver(host,user,passwd,database,port)
                    sqlserver_data = sqlserver.select_SQL_Db(instance_sql)[0][0]
                    print(sqlserver_data)


if __name__=="__main__":
    zbx = Zabbix()
    data = zbx.db_id_switch_name(191)
    print(data)

    # 根据获取到的db_name在数据库中查找instance_id信息。
    # sql_id = "select instance_id from db_info where db_name={0}".format(message[4])
    # data = self.exmysql.insert_mysql_Db(sql_id)
    # print(data)

    # 根据instance_id信息查询数据库ip，端口等信息
    # sql_info = "select instance_ip_addr,instance_db_port,instance_user_name,instance_passwd from isntance_info where instace_id='{0}'".format(data[0][0])
    # instance_info = self.exmysql.insert_mysql_Db(sql_info)
    # host = instance_info[0][0]
    # port = instance_info[0][1]
    # user = instance_info[0][2]
    # passwd = instance_info[0][3]
    # database = 'E6manageDB'

    # 连接sqlserver执行sql并返回结果。
    # SQL = Data_SQLserver(host,user,passwd,database,port)
    # value = SQL.select_SQL_Db(message[1])
    # print(value)

