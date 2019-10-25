from App.Model.Mssql import *


class querySql(object):
    def __init__(self,connectInfo):
        self.connectInfo = connectInfo
        self.host = self.connectInfo[0][1][0][7]
        self.user = self.connectInfo[0][1][0][9]
        self.passwd = self.connectInfo[0][1][0][10]
        self.port = self.connectInfo[0][1][0][8]
        self.conn_dbname = 'E6ManagerDB'
        self.DBsql = Data_SQLserver(self.host, self.user, self.passwd, self.conn_dbname, self.port)
    def QueryDBName(self,sql):
        DbName = self.DBsql.select_SQL_Db(sql)
        return DbName