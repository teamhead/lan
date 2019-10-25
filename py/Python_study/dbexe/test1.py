import pymysql
import pymssql

class Data_mysql(object):
    def __init__(self,host,username,password,database,port):
        self.host = host
        self.username = username
        self.password = password
        self.database = database
        self.port = port
        self.db = pymysql.connect(self.host,self.username,self.password,self.database,self.port,charset='utf8')
        self.SQLINT = {}
        self.SQLSTR = {}

    def select_mysql_Db(self,sql):
        ''' MYsql数据库查询 '''
        self.cursor = self.db.cursor()
        try:
            self.cursor.execute(sql) 
            datas = self.cursor.fetchall()
            return datas
        except:
            print('Error: unable to fecth data')
        finally:
            self.cursor.close()

    def closeDb(self):
        ''' 数据库连接关闭 '''
        self.db.close()

    def Getjson_MYSQL(self,sql):
        datas = self.select_mysql_Db(sql)
        print(datas)
        for data in datas:
            if data[0] == 'int' :
                self.SQLINT['{#SQLLINT}'] = data[2]
            elif data[0] == 'str':
                self.SQLSTR['{#SQLLSTR}'] = data[2]
            else:
                pass

class Data_SQLserver(object):
    def __init__(self,server,username,password,database,port):
        self.server = server
        self.user = username
        self.password = password
        self.database = database
        self.port = port
        self.db = pymssql.connect(server=self.server, port=self.port, user=self.user, password=self.password, database=self.database)

    def select_SQL_Db(self,sql):
        ''' SQLserver数据库查询 '''
        self.db.autocommit(True)
        self.cursor = self.db.cursor()
        try:
            self.cursor.execute(sql)
            datas = self.cursor.fetchall()

            print(datas)
            return datas
        except Exception as e:
            print(e)
            print('Error: unable to fecth data')
        # finally:
        #     self.cursor.close()

if __name__ == '__main__':


    # 查询mysql数据库表中的信息
    # Dbmysql = Data_mysql('rm-wz9954fkn5h96zerz.mysql.rds.aliyuncs.com','db_mng_user','X2rePFHQaY-mGEdFcCM9n','db_manage_pfm',3306)
    # mysql = "select type,mon_interval,monitorkey from zabbix_monitor_config where type='int'"
    # Dbmysql.Getjson_MYSQL(mysql)


    # 获取SQLserver执行后的结果
    host = '10.100.1.219'  # info.Instance_info.instance_ip_addr
    user = 'dbmg_user'  # info.instance_user_name
    passswd = 'vkFsrtsEu5Q-lWta1vlVi'  # info.instance_passwd
    db = 'E6ManagerDB'
    port = '8889'  # info.instance_db_port
    DBsql = Data_SQLserver(host, user, passswd, db, port)
    sql = 'select name from sys.databases;'
    sql1=r"exec BR.prBKandRestoreDBAll @DatabaseNames = N'E6ETmsNew',@BKFileUrl = N'D:\temp',@BKDBKey = N'321',@OperType = N'BK',@BKMode=0,@RSMode= 0,@RSOper= 0, @DBFileUrl= N'D:\SQLDB',@LogFileUrl= N'D:\SQLLOG',@UserName='S_DLBUSER',@PassWD='123',@OperMode=0"
    sql2 = r"""exec BR.prBKandRestoreDBAll @DatabaseNames = N'E6ETmsBms',@BKFileUrl = N'D:\temp',@BKDBKey = N'测试数据',@OperType = N'BK',@BKMode=0,@RSMode= 0,@RSOper= 0, @DBFileUrl= N'D:\SQLDB',@LogFileUrl= N'D:\SQLLOG',@UserName='S_DLBUSER',@PassWD='123456',@OperMode=0"""
    DBsql.select_SQL_Db(sql1)
    # print(DBsql.select_SQL_Db(sql1))