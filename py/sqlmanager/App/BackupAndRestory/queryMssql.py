from App.Model.Mssql import *
from App.BackupAndRestory.queryMysql import *
from App.BackupAndRestory.backupAndRestore import *


class ExeInfo(object):
	def __init__(self, connectInfo):
		self.connectInfo = connectInfo['info']
		self.host = self.connectInfo['host']
		self.user = self.connectInfo['user']
		self.passwd = self.connectInfo['passwd']
		self.port = self.connectInfo['port']
		self.conn_dbname = 'E6ManagerDB'
		self.DBsql = Data_SQLserver(self.host, self.user, self.passwd, self.conn_dbname, self.port)

	# 执行sql
	def exeSql(self, sql, backup_list):
		data = self.DBsql.select_SQL_Db(sql)
		if data[0][0] == 0:
			mysql = QueryInfo()
			name = ''
			print(backup_list)
			for dbname in backup_list['selectData']:
				name += dbname + ','
			args = {'operationName': backup_list['exe_result'], 'operationType': backup_list['back_type'],
			        'db_name': name,
			        'instance_id': backup_list['instance_id'], 'executiveDescribed': '执行成功', 'executingState': 0}
			BKARS = BackupAndRestore()
			insql = BKARS.BackUpStartSql(backup_list, args)
			data_ins = mysql.exeSql(insql)
			print(data_ins)
		elif data[0][0] == 1:
			mysql = Data_mysql()
			name = ''
			for dbname in backup_list['db_name']:
				name += dbname + ','
			args = {'operationName': backup_list['exe_result'], 'operationType': backup_list['back_type'],
			        'db_name': name,
			        'instance_id': backup_list['instance_id'], 'executiveDescribed': data[0][1],
			        'executingState': 0}
			BKARS = BackupAndRestore()
			insql = BKARS.BackUpStartSql(backup_list, args)
			data = mysql.insert_mysql_Db(insql)
			if data[0][0] == 0:
				print('记录插入成功')
			elif data[0][1] == 1:
				print('插入记录失败')

	# 执行查询sql
	def querySql(self, typeid, backup_list):
		# 备份类型为全备
		if typeid == 'back_all':
			message_sql = {}
			for db_name in backup_list['selectData']:
				sqlserver = "select FullBKResStmt from BR.DBBackupInfo where DBName='{0}'".format(db_name)
				sql = self.DBsql.select_SQL_Db(sqlserver)
				if sql[0][0] == 1:
					sql = sql[0][1]
				message_sql[db_name] = sql
			return message_sql
		# 备份类型为日志
		elif typeid == 'back_log':
			message_sql = {}
			for db_name in backup_list['selecetData']:
				sqlserver = "select LogBKResStmt from BR.DBBackupInfo where DBName='{0}'".format(db_name)
				sql = self.DBsql.select_SQL_Db(sqlserver)
				if sql[0][0] == 1:
					sql = sql[0][1]
				message_sql[db_name] = sql
			return message_sql
		# 备份类型为差异
		elif typeid == "back_diff":
			message_sql = {}
			for db_name in backup_list['selectData']:
				sqlserver = "select DiffBKResStmt from BR.DBBackupInfo where DBName='{0}'".format(db_name)
				sql = self.DBsql.select_SQL_Db(sqlserver)
				if sql[0][0] == 1:
					sql = sql[0][1]
				message_sql[db_name] = sql
			return message_sql
		else:
			message_sql = ''
			return message_sql

	# 查询处理用户语句
	def queryUserSql(self, userInfo_list):
		message_sql = {}
		for db_name in userInfo_list['selectData']:
			sqlserver = "select LoginUserStmt from BR.DBBackupInfo where DBName='{0}'".format(db_name)
			sql = self.DBsql.select_SQL_Db(sqlserver)
			if sql[0][0] == 1:
				sql = sql[0][1]
			message_sql[db_name] = sql
		return message_sql
