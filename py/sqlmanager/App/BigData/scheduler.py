from App.BigData.parse import *
from App.Model.Mssql import *


class Sche(object):
	def __init__(self):
		self.cursor = Data_SQLserver('58.61.34.213', 'S_SQLManager', 'YhwNJ4ddxiS3-ICGNCOMe', 'E6ManagerDB', 8089)

	def insertBGDT(self, data):
		parse = Parsedata()
		sql = parse.insertSQL(data)
		data = self.cursor.select_SQL_Db(sql)
		return data

	def queryALLBGDT(self, data=''):
		parse = Parsedata()
		if data == '':
			sql = parse.queryAllSQL()
			data = self.cursor.select_SQL_Db(sql)
			info = []
			for messages in data:
				message = {}
				message['SourceServerIP'] = messages[1]
				message['SyncDBName'] = messages[2]
				message['SyncSchemaName'] = messages[3]
				message['SyncTableName'] = messages[4]
				message['QueryOutURL'] = messages[5]
				message['SourceUser'] = messages[6]
				message['SourcePW'] = messages[7]
				message['TargetServerIP'] = messages[8]
				message['TargetDBName'] = messages[9]
				message['UpdateTime'] = messages[10]
				message['IsEnableFlag'] = messages[11]
				message['WriteTime'] = messages[12]
				message['TargetTableName'] = messages[13]
				message['SyncSource'] = messages[14]
				message['SyncTarget'] = messages[15]
				message['TargetUser'] = messages[16]
				message['TargetPW'] = messages[17]
				message['SourceCols'] = messages[18]
				message['TargetCols'] = messages[19]
				message['SourceCondition'] = messages[20]
				message['TargetPresql'] = messages[21]
				message['SourceTableName'] = messages[22]
				message['SyncType'] = messages[23]
				message['PKID'] = messages[24]
				message['SyncFrequence'] = messages[25]
				message['TargetPostsql'] = messages[26]
				message['SyncCategory'] = messages[27]
				message['QuerySql'] = messages[28]
				message['Remark'] = messages[29]
				message['id'] = messages[0]
				info.append(message)
			return info
		else:
			sql = parse.querySQL(data)
			data = self.cursor.select_SQL_Db(sql)
			info = []
			for messages in data:
				message = {}
				message['SourceServerIP'] = messages[1]
				message['SyncDBName'] = messages[2]
				message['SyncSchemaName'] = messages[3]
				message['SyncTableName'] = messages[4]
				message['QueryOutURL'] = messages[5]
				message['SourceUser'] = messages[6]
				message['SourcePW'] = messages[7]
				message['TargetServerIP'] = messages[8]
				message['TargetDBName'] = messages[9]
				message['UpdateTime'] = messages[10]
				message['IsEnableFlag'] = messages[11]
				message['WriteTime'] = messages[12]
				message['TargetTableName'] = messages[13]
				message['SyncSource'] = messages[14]
				message['SyncTarget'] = messages[15]
				message['TargetUser'] = messages[16]
				message['TargetPW'] = messages[17]
				message['SourceCols'] = messages[18]
				message['TargetCols'] = messages[19]
				message['SourceCondition'] = messages[20]
				message['TargetPresql'] = messages[21]
				message['SourceTableName'] = messages[22]
				message['SyncType'] = messages[23]
				message['PKID'] = messages[24]
				message['SyncFrequence'] = messages[25]
				message['TargetPostsql'] = messages[26]
				message['SyncCategory'] = messages[27]
				message['QuerySql'] = messages[28]
				message['Remark'] = messages[29]
				message['id'] = messages[0]
				info.append(message)
			return info

	def updataBigData(self, data):
		parse = Parsedata()
		sql = parse.updataSQL(data)
		print(sql)
		message = self.cursor.select_SQL_Db(sql)
		if message == "Statement not executed or executed statement has no resultset":
			messages = {'code': 0, 'msg': 'ok'}
		return messages

	def deleteBigData(self, data):
		parse = Parsedata()
		sql = parse.deleteSQL(data)
		data = self.cursor.select_SQL_Db(sql)
		return data
