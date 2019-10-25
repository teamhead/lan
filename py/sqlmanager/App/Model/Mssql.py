import pymssql


class Data_SQLserver(object):
	def __init__(self, server, username, password, database, port):
		'''初始化sqlserver信息'''
		self.server = server
		self.user = username
		self.password = password
		self.database = database
		self.port = port
		self.db = pymssql.connect(server = self.server, port = self.port, user = self.user, password = self.password,
		                          database = self.database, charset = "utf8")

	def select_SQL_Db(self, sql):
		''' SQLserver数据库查询 '''
		self.db.autocommit(True)
		self.cursor = self.db.cursor()
		try:
			self.cursor.execute(sql)
			datas = self.cursor.fetchall()
			return datas
		except Exception as e:
			data = [(1, str(e))]
			return data
