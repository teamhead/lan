'''
作者：兰嘉轩
创建时间: 2019年8月19日
描述: 封装数据库备份还原创建用户等方法。此类方法基于存储过程实现。
'''
from App.Model.model import *

class BackupAndRestore(object):
    def __init__(self,host, user, passwd, port,backup_list=[]):
        # 初始化连接数据库信息
        self.host = host
        self.user = user
        self.passwd = passwd
        self.port = port
        self.conn_dbname = 'E6ManagerDB'
        # 初始化存储过程变量
        self.backup_list = backup_list
        # self.db_name = ''
        self.OperType_dict = {'创建目录': 'MD', '备份': 'BK', '还原': 'RS', '创建账户': 'CU'}
        self.BKMode_dict = {'全备':0,'差异':1,'日志':2}
        self.RSOper_dict = {'完全还原':0,'不完全还原':1}
        self.OperMode_dict = {'处理孤立用户': 0, '新建用户授权': 1}
        self.db_name_list=[]
        # 判断用户输入是否有备份需要的字段信息。
        if backup_list:
            print(backup_list)
            for back_up in backup_list:
                if back_up['name']=='instance_name':
                    instance_name=back_up['value']
                elif back_up['name'] == "db_name":
                    self.db_name = back_up['value']
                    self.db_name_list.append(self.db_name)
                elif back_up['name'] == 'BKFileUrl':
                    self.BKFileUrl = back_up['value']
                elif back_up['name'] == 'BKDBKey':
                    self.BKDBKey = back_up['value']
                elif back_up['name'] == 'OperType':
                    self.OperType = self.OperType_dict[back_up['value']]
                elif back_up['name'] == 'BKMode':
                    self.BKMode = self.BKMode_dict[back_up['value']]
                elif back_up['name'] == 'RSMode':
                    self.RSMode = self.BKMode_dict[back_up['value']]
                elif back_up['name'] == 'RSOper':
                    self.RSOper = self.RSOper_dict[back_up['value']]
                elif back_up['name'] == 'DBFileUrl':
                    self.DBFileUrl = back_up['value']
                elif back_up['name'] == 'LogFileUrl':
                    self.LogFileUrl = back_up['value']
                elif back_up['name'] == 'UserName':
                    self.UserName = back_up['value']
                elif back_up['name'] == 'PassWD':
                    self.PassWD = back_up['value']
                elif back_up['name'] == 'OperMode':
                    self.OperMode = self.OperMode_dict[back_up['value']]
                elif back_up['name'] == "RSFileUrl":
                    self.RSFileUrl = back_up['value']
                elif back_up['name'] == 'show-sql':
                    self.show_sql = back_up['value']
        else:
            print('未获取到数据')

    # 更新mysql上的db_info
    def update_db_info(self,easname):
        # 初始化数据库信息，查询选中的源数据库的信息
        Dbmysql = Data_mysql(self.host,self.user,self.passwd,'db_manage_pfm',self.port)
        mysql = "select instance_ip_addr,instance_db_port,instance_user_name,instance_passwd,instance_id from instance_info where instance_name='%s'" % easname
        print(mysql)
        datas = Dbmysql.select_mysql_Db(mysql)
        if datas:
            host = datas[0][0]
            port = datas[0][1]
            user = datas[0][2]
            passwd = datas[0][3]
            instance_id = datas[0][4]
            databse = 'E6ManagerDB'
            # 连接目标数据库，查询除系统数据库以外的数据库名
            DBsql = Data_SQLserver(host, user, passwd, databse, port)
            SQLsql = "select name from sys.databases where name not in('master','Model','msdb','tempdb')"
            print(SQLsql)
            data_names = DBsql.select_SQL_Db(SQLsql)
            # 判断是否存在数据库名和对应实例id存在一致的情况
            mysql_querydbname = "select db_name from db_info where instance_id={0}".format(instance_id)
            data_querydbnames = Dbmysql.select_mysql_Db(mysql_querydbname)
            print(data_querydbnames)
            # 判断源段数据库存在数据库时执行
            if data_names:
                for data_name in data_names:
                    # 如果存在数据库名和对应实例id一致的情况，则更新数据库名信息
                    if data_querydbnames:
                        mysql2 = "UPDATE db_info SET modified_time=now() where db_name='{0}'".format(data_name[0])
                        Dbmysql.insert_mysql_Db(mysql2)
                        print(data_name[0] + '同步成功')
                    # 如果不存在，插入新的数据库名至本地表
                    else:
                        mysql1 = "insert into db_info(db_name,db_backup_path,instance_id) values('{0}','/admin','{1}')".format(
                            data_name[0], instance_id)
                        Dbmysql.insert_mysql_Db(mysql1)
                        print(data_name[0] + '同步成功')
            print('共计' + str(len(data_names)) + '条')

    # 生成sql语句
    def get_sql(self):
        print(len(self.db_name_list))
        db_names = ''
        # 拼接成db_name以逗号分隔开的字符串
        for db_name_source in self.db_name_list:
            db_names += db_name_source+','
        # 判断是否是还原操作
        if self.OperType=="RS":
            DBsql = Data_SQLserver(self.host, self.user, self.passwd, self.conn_dbname, self.port)
            sqlserver = r"exec BR.prBKandRestoreDBAll @DatabaseNames = N'{0}',@BKFileUrl='{1}',@BKDBKey = N'{2}',@OperType = N'{3}',@RSMode={4},@RSOper= {5},@DBFileUrl='{6}',@LogFileUrl= N'{7}',@RSFileUrl=N'{8}'".format(
                db_names,self.BKFileUrl, self.BKDBKey, self.OperType, self.RSMode, self.RSOper, self.DBFileUrl,self.LogFileUrl,self.RSFileUrl)
            DBsql.select_SQL_Db(sqlserver)
            # 判断还原类型
            if self.RSMode == 0:
                # 捕获查询源端查询语句时的错误
                try:
                    message_sql = ''
                    # 循环用户勾选的数据库信息。并依次取出还原语句，并拼成可用的还原语句。
                    for db_name_source_l in self.db_name_list:
                        print(db_name_source_l)
                        sqlserver_1 = "select FullBKResStmt from BR.DBBackupInfo where DBName='{0}'".format(db_name_source_l)
                        message_sql += DBsql.select_SQL_Db(sqlserver_1)[0][0]+"#"
                    return message_sql
                # 执行过程中出错，将错误返回给前端。
                except Exception as e:
                    message_sql = e
                    return message_sql
            # 判断是否为差异
            elif self.RSMode == 1:
                message_sql = ''
                for db_name_source_l in self.db_name_list:
                    sqlserver_1 = "select DiffBKResStmt from BR.DBBackupInfo where DBName='{0}'".format(db_name_source_l)
                    message_sql += DBsql.select_SQL_Db(sqlserver_1)[0][0]+"#"
                return message_sql
            # 判断是否为日志
            elif self.RSMode == 2:
                message_sql = ''
                for db_name_source_l in self.db_name_list:
                    sqlserver_1 = "select LogBKResStmt from BR.DBBackupInfo where DBName='{0}'".format(db_name_source_l)
                    message_sql += DBsql.select_SQL_Db(sqlserver_1)[0][0]+"#"
                return message_sql
            else:
                print('请选择还原模式')
        # 判断是否是创建用户
        elif self.OperType=="CU":
            DBsql = Data_SQLserver(self.host, self.user, self.passwd, self.conn_dbname, self.port)
            sqlserver = r"exec BR.prBKandRestoreDBAll @DatabaseNames = N'{0}',@BKDBKey = N'{1}',@OperType='{2}',@UserName='{3}',@PassWD='{4}',@OperMode='{5}',@BKFileUrl='{6}',@RSFileUrl='{7}'".format(
                db_names, self.BKDBKey, self.OperType, self.UserName, self.PassWD, self.OperMode, self.BKFileUrl,self.RSFileUrl)
            DBsql.select_SQL_Db(sqlserver)
            message_sql = ''
            for db_name_l in  self.db_name_list:
                sqlserver_1 = "select LoginUserStmt from BR.DBBackupInfo where DBName='{0}'".format(db_name_l)
                CU_str = DBsql.select_SQL_Db(sqlserver_1)
                message_sql += CU_str[0][0] +"#"
            return message_sql
        else:
            message_sql = "缺少字段"
            return message_sql


    # 备份数据库
    def backup(self):
        if self.RSFileUrl=='':
            self.RSFileUrl=self.BKFileUrl
        DBsql = Data_SQLserver(self.host, self.user, self.passwd, self.conn_dbname, self.port)
        sqlserver = r"exec BR.prBKandRestoreDBAll @DatabaseNames = N'{0}',@BKFileUrl = N'{1}',@BKDBKey = N'{2}',@OperType = N'{3}',@RSMode={4},@DBFileUrl= N'{5}',@LogFileUrl= N'{6}',@RSFileUrl=N'{7}'".format(
            self.db_name, self.BKFileUrl, self.BKDBKey, self.OperType, self.BKMode, self.DBFileUrl, self.LogFileUrl,self.RSFileUrl)
        DBsql.select_SQL_Db(sqlserver)

    # 还原数据库或者创建用户
    def restore(self):
        DBsql = Data_SQLserver(self.host, self.user, self.passwd, self.conn_dbname, self.port)
        sql_server = self.show_sql.split('#')
        for sql in sql_server:
            print(sql)
            if sql=='':
                pass
            else:
                try:
                    data = DBsql.select_SQL_Db(sql)
                    print(data)
                except Exception as e:
                    print(e)
                    print('执行失败')
    # 创建用户
    def create_user(self):
        if self.BKFileUrl =='':
            self.BKFileUrl = r'D:\temp'
        if self.RSFileUrl=='':
            self.RSFileUrl=self.BKFileUrl
        DBsql = Data_SQLserver(self.host, self.user, self.passwd, self.conn_dbname, self.port)
        sqlserver = r"exec BR.prBKandRestoreDBAll @DatabaseNames = N'{0}',@BKDBKey = N'{1}',@OperType='{2}',@UserName='{3}',@PassWD='{4}',@OperMode='{5}',@BKFileUrl='{6}',@RSFileUrl='{7}'".format(
            self.db_name,self.BKDBKey, self.OperType, self.UserName, self.PassWD, self.OperMode,self.BKFileUrl,self.RSFileUrl)
        print(sqlserver)
        DBsql.select_SQL_Db(sqlserver)

if __name__ == "__main__":
    '''以下为测试数据，调用此类，该代码不执行'''
    backup_list = [{'name': 'OperType', 'value': '备份'}, {'name': 'instance_name', 'value': 'centos1'}, {'name': 'db_name', 'value': 'crvplateform'}, {'name': 'BKFileUrl', 'value': 'D:\\temp'}, {'name': 'BKDBKey', 'value': ''}, {'name': 'BKMode', 'value': '全备'}, {'name': 'RSMode', 'value': '全备'}, {'name': 'RSOper', 'value': '完全还原'}, {'name': 'DBFileUrl', 'value': ''}, {'name': 'LogFileUrl', 'value': ''}, {'name': 'UserName', 'value': ''}, {'name': 'PassWD', 'value': ''}, {'name': 'OperMode', 'value': '0:处理孤立用户'}]
    BKARS = BackupAndRestore(host='10.100.1.219',user= 'dbmg_user',passwd= 'vkFsrtsEu5Q-lWta1vlVi',port=8889,backup_list=backup_list)
    BKARS.backup()
