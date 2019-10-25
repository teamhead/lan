class Parsedata(object):
	def insertSQL(self, data):
		sql = '''insert into [bcp].[BcpSyncList](
     [SourceServerIP]
      ,[SyncDBName]
      ,[SyncSchemaName]
      ,[SyncTableName]
      ,[QueryOutURL]
      ,[SourceUser]
      ,[SourcePW]
      ,[TargetServerIP]
      ,[TargetDBName]
	  ,[UpdateTime]
      ,[IsEnableFlag]
	  ,[WriteTime]
      ,[TargetTableName]
      ,[SyncSource]
      ,[SyncTarget]
      ,[TargetUser]
      ,[TargetPW]
      ,[SourceCols]
      ,[TargetCols]
      ,[SourceCondition]
      ,[TargetPresql]
      ,[SourceTableName]
      ,[SyncType]
      ,[PKID]
      ,[SyncFrequence]
      ,[TargetPostsql]
      ,[SyncCategory]
      ,[QuerySql]
      ,[Remark] )
	   values('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}',GETDATE(),{9},GETDATE(),'{10}','{11}','{12}','{13}','{14}','{15}','{16}','{17}','{18}','{19}','{20}','{21}',{22},'{23}','{24}','{25}','{26}')'''.format(
				data['SourceServerIP'], data['SyncDBName'], data['SyncSchemaName'],
				data['SyncTableName'], data['QueryOutURL'], data['SourceUser'],
				data['SourcePW'], data['TargetServerIP'], data['TargetDBName'],
				data['IsEnableFlag'], data['TargetTableName'], data['SyncSource'],
				data['SyncTarget'], data['TargetUser'], data['TargetPW'],
				data['SourceCols'], data['TargetCols'], data['SourceCondition'],
				data['TargetPresql'], data['SourceTableName'], data['SyncType'],
				data['PKID'], data['SyncFrequence'], data['TargetPostsql'],
				data['SyncCategory'], data['QuerySql'], data['Remark']
		)
		return sql

	def querySQL(self, data):
		where = ''
		print(data.keys())
		for key in data.keys():
			if len(data.keys()) == 1:
				where += ' ' + key + '=' + str(data[key]) + ' '
			else:
				where += ' ' + key + '=' + str(data[key]) + ' ' + 'and' + ' '

		sql = ('''select * from [bcp].[BcpSyncList] where''' + where).rstrip('and ')
		print(sql)
		return sql

	def queryAllSQL(self):
		sql = "select * from [bcp].[BcpSyncList]"
		return sql

	def updataSQL(self, data):
		sql = '''update [bcp].[BcpSyncList] set
    [SourceServerIP]='{0}'
      ,[SyncDBName]='{1}'
      ,[SyncSchemaName]='{2}'
      ,[SyncTableName]='{3}'
      ,[QueryOutURL]='{4}'
      ,[SourceUser]='{5}'
      ,[SourcePW]='{6}'
      ,[TargetServerIP]='{7}'
      ,[TargetDBName]='{8}'
	  ,[UpdateTime]=getdate()
      ,[IsEnableFlag]={9}
	  ,[WriteTime]=getdate()
      ,[TargetTableName]='{10}'
      ,[SyncSource]='{11}'
      ,[SyncTarget]='{12}'
      ,[TargetUser]='{13}'
      ,[TargetPW]='{14}'
      ,[SourceCols]='{15}'
      ,[TargetCols]='{16}'
      ,[SourceCondition]='{17}'
      ,[TargetPresql]='{18}'
      ,[SourceTableName]='{19}'
      ,[SyncType]='{20}'
      ,[PKID]='{21}'
      ,[SyncFrequence]={22}
      ,[TargetPostsql]='{23}'
      ,[SyncCategory]='{24}'
      ,[QuerySql]='{25}'
      ,[Remark]='{26}'
       where Rid = {27}'''.format(
				data['SourceServerIP'], data['SyncDBName'], data['SyncSchemaName'],
				data['SyncTableName'], data['QueryOutURL'], data['SourceUser'],
				data['SourcePW'], data['TargetServerIP'], data['TargetDBName'],
				data['IsEnableFlag'], data['TargetTableName'], data['SyncSource'], data['SyncTarget'],
				data['TargetUser'], data['TargetPW'], data['SourceCols'],
				data['TargetCols'], data['SourceCondition'], data['TargetPresql'],
				data['SourceTableName'], data['SyncType'], data['PKID'], data['SyncFrequence'],
				data['TargetPostsql'], data['SyncCategory'], data['QuerySql'],
				data['Remark'], data['id']
		)
		return sql

	def deleteSQL(self, data):
		pass
