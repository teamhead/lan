from App.Model.Mysql import *
import json


# 初始化连接信息
class QueryInfo(object):
    def __init__(self,info=''):
        self.info = info
        self.HOST = '127.0.0.1'
        self.USER = 'db_mng_user'
        self.PASSWD = 'X2rePFHQaY-mGEdFcCM9n'
        self.DBNAME = 'db_manage_pfm'
        self.PORT = 3306
        self.query =Data_mysql(self.HOST,self.USER,self.PASSWD,self.DBNAME,self.PORT)

    # 根据实例名查询实例信息
    def nameInstance(self):
        sql = "select instance_ip_addr,instance_db_port,instance_user_name,instance_passwd from instance_info where instance_id='{0}'".format(self.info)
        data = self.query.select_mysql_Db(sql)
        print(data)
        if data:
            host = data[0][1][0][0]
            port = data[0][1][0][1]
            user = data[0][1][0][2]
            passwd = data[0][1][0][3]
            instance_content = {'code':0,'info':{'host':host,'port':port,'user':user,'passwd':passwd}}
            return instance_content
        else:
            result = {'code':1,'info':'无此实例信息'}
            return result
    def exeSql(self,sql):
        print(sql)
        data = self.query.insert_mysql_Db(sql)
        if data[0][0] == 0:
            message = 'successful'
            return message
        elif data[0][0] == 1:
            message = str(data[0][1])
            return message
    def insertLOG(self,sql):
        data = self.query.insert_mysql_Db(sql)
        return data


