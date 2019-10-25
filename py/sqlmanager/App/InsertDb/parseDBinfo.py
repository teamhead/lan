

class ParseDbInfo(object):
    def getDbInfoSql(self,instanceInfo):
        mysql = "select db_name,db_id from instance_info a inner join db_info b on a.instance_id=b.instance_id where a.isvalid=1 and b.isvalid=1 and a.instance_name='%s'"%instanceInfo['name']
        return mysql
    def queryDBSql(self):
        sql = "select name from sys.databases where name not in ('master','tempdb','model','msdb')"
        return sql
    def InstanceInfoSql(self,instanceName):
        mysql = "select * from instance_info where instance_id='{0}'".format(instanceName)
        return mysql
    def insertDbSql(self,dbname,instanceId):
        mysql = "insert into db_info(db_name,db_backup_path,instance_id) values('{0}','/admin','{1}')".format(dbname,instanceId)
        return mysql