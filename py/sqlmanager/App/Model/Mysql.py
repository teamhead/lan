import pymysql

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
            data = [(0,self.cursor.fetchall())]
            return data
        except Exception as e:
            data = [(1, str(e))]
            return data
        finally:
            self.cursor.close()

    def insert_mysql_Db(self,sql):
        ''' MYsql数据库查询 '''
        self.cursor = self.db.cursor()
        try:
            datas = self.cursor.execute(sql)
            self.db.commit()
            data = [(0,datas)]
            return data
        except Exception as e:
            data = [(1, str(e))]
            return data
        finally:
            self.cursor.close()


    def update_mysql_Db(self,sql):
        self.cursor = self.db.cursor()
        try:
            datas=self.cursor.execute(sql)
            self.db.commit()
            data = [(0,datas)]
            return data
        except Exception as e:
            data = [(1, str(e))]
            return data
        finally:
            self.cursor.close()


    def closeDb(self):
        ''' 数据库连接关闭 '''
        self.db.close()

    # 以下分解数据库信息的方法
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


    def parse_db(self,data):
        '''db_info'''
        if data['created_user_id']:
            created_user_id = data['created_user_id']
        elif data['created_user_id']:
            created_time = data['created_time']
        elif data['created_user_id']:
            modified_user_id = data['modified_user_id']
        elif data['created_user_id']:
            modified_time = data['modified_time']
        elif data['created_user_id']:
            isvalid = data['isvalid']
        elif data['created_user_id']:
            db_id = data['db_id']
        elif data['created_user_id']:
            db_name = data['db_name']
        elif data['created_user_id']:
            db_backup_path = data['db_backup_path']
        elif data['created_user_id']:
            instance_id = data['instance_id']

