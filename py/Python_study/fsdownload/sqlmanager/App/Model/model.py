'''
作者：兰嘉轩
创建时间: 2019年8月19日
描述: 封装mysql、sqlserver查询插入等功能方法，此类可单独取出使用。
'''


import pymysql
import pymssql

# 连接mysql
# ===========================================================================================================================================
class Data_mysql(object):
    '''初始化mysql连接信息'''
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
        except Exception as e:
            print(e)
            print('Error: unable to fecth data')
        finally:
            self.cursor.close()
    def insert_mysql_Db(self,sql):
        ''' MYsql数据库查询 '''
        self.cursor = self.db.cursor()
        try:
            self.cursor.execute(sql)
            datas = self.cursor.fetchall()
            self.db.commit()
            return datas
        except Exception as e:
            print(e)
            print('Error: unable to fecth data')
        finally:
            self.cursor.close()
    def update_mysql_Db(self,sql,easname):
        self.cursor = self.db.cursor()
        try:
            self.cursor.execute(sql)
        except Exception as e:
            print(e)



    def closeDb(self):
        ''' 数据库连接关闭 '''
        self.db.close()

    def Getjson_MYSQL(self,sql):
        '''拼接监控方法'''
        datas = self.select_mysql_Db(sql)
        print(datas)
        for data in datas:
            if data[0] == 'int' :
                self.SQLINT['{#SQLLINT}'] = data[2]
            elif data[0] == 'str':
                self.SQLSTR['{#SQLLSTR}'] = data[2]
            else:
                pass
# =============================================================================================================================
# 连接SQLSERVER
class Data_SQLserver(object):
    def __init__(self,server,username,password,database,port):
        '''初始化sqlserver信息'''
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
            return datas
        except Exception as e:
            print(e)
            print('Error: unable to fecth data')
            return e

        # finally:
        #     self.cursor.close()

if __name__ == '__main__':
    # 查询mysql数据库表中的信息
    # Dbmysql = Data_mysql('rm-wz9954fkn5h96zerz.mysql.rds.aliyuncs.com','db_mng_user','X2rePFHQaY-mGEdFcCM9n','db_manage_pfm',3306)
    # mysql1 = "select * from zabbix_monitor_config where monitorkey='查询结果为0则报警'"
    # mysql = "insert into instance_info(instance_name,instance_ip_addr,instance_db_port,instance_user_name,instance_passwd) values('centos1','10.100.1.219','8889','dbmg_user','123456')"
    # data = Dbmysql.insert_mysql_Db(mysql1)
    # print(data)

    # 获取SQLserver执行后的结果
    # host = '10.100.1.219'  # info.Instance_info.instance_ip_addr
    # user = 'dbmg_user'  # info.instance_user_name
    # passswd = 'vkFsrtsEu5Q-lWta1vlVi'  # info.instance_passwd
    # db = 'E6ManagerDB'
    # port = '8889'  # info.instance_db_port
    # DBsql = Data_SQLserver(host, user, passswd, db, port)
    # sql = 'select name from sys.databases;'
    # sql2 = r"exec BR.prBKandRestoreDBAll @DatabaseNames = N'E6ETmsBms',@BKFileUrl = N'D:\temp',@BKDBKey = N'测试数据',@OperType = N'BK',@BKMode=0,@RSMode= 0,@RSOper= 0, @DBFileUrl= N'D:\SQLDB',@LogFileUrl= N'D:\SQLLOG',@UserName='S_DLBUSER',@PassWD='123',@OperMode=0"
    # data = DBsql.select_SQL_Db(sql2)
    # print(data)
    # sql = "select * from zabbix_monitor_config"
    # Dbmysql.select_mysql_Db(sql)
    sql = Data_SQLserver('10.100.1.2','s_manage_user','0aH94H3p-xidpCBB37uAK','E6ManagerDB',8088)
    sql_l =r'''RESTORE DATABASE E6CTF FROM  DISK = N'E:\temp1\E6CTF_20190819100849.bak' WITH MOVE N'E6CTF' TO N'E:\SQLDB_8.222\E6CTF.mdf', MOVE N'E6CTF_log' TO N'E:\SQLDB_8.222\E6CTF_log.ldf', NOUNLOAD,STATS = 10,RECOVERY'''
    sql.select_SQL_Db(sql_l)