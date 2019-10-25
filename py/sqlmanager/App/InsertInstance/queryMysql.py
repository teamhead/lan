from App.Model.Mysql import *

class QueryInfo(object):
    def __init__(self):
        self.HOST = '127.0.0.1'
        self.USER = 'db_mng_user'
        self.PASSWD = 'X2rePFHQaY-mGEdFcCM9n'
        self.DBNAME = 'db_manage_pfm'
        self.PORT = 3306
        self.query =Data_mysql(self.HOST,self.USER,self.PASSWD,self.DBNAME,self.PORT)
    def exeSqlinsert(self,sql):
        result = self.query.insert_mysql_Db(sql)
        return result
    def exeSql(self,sql):
        result = self.query.select_mysql_Db(sql)
        return result
