from .parseDBinfo import *
from .QueryMysql import *
from .QueryMssql import *

class Sche(object):
    '''查询数据库信息'''
    def queryDB(self,instanceInfo):
        getSql = ParseDbInfo()
        mysql = getSql.getDbInfoSql(instanceInfo)
        exeSql = Exesql()
        datas = exeSql.queryDB(mysql)
        DbInfo_list = []
        for data in datas[0][1]:
            dbinfo = {}
            dbinfo['db_name']=data[0]
            dbinfo['db_id'] = data[1]
            DbInfo_list.append(data[0])
        return DbInfo_list

    def insert_Db(self,result):
        '''添加数据库信息'''
        instance_name = result
        print(instance_name)
        # 创建生成语句对象
        createSQL = ParseDbInfo()
        # 生成查询instanceinfo语句
        mysql= createSQL.InstanceInfoSql(instance_name)
        # 生成查询数据库名语句
        sql = createSQL.queryDBSql()
        print(sql)
        # 创建查询实例信息对象
        queryInstance = Exesql()
        # 查询实例信息
        instanceInfo = queryInstance.queryDB(mysql)
        print(instanceInfo)
        # 创建实例信息查询dbname
        queryDbname = querySql(instanceInfo)
        # 查询dbname
        DbName = queryDbname.QueryDBName(sql)
        print(DbName)
        # 创建插入数据库名语句
        insertDb = Exesql()
        # 获取插入实例信息语句并插入数据
        for dbname in DbName:
            mysql = createSQL.insertDbSql(dbname[0],instance_name)
            data = insertDb.insertDB(mysql)
        return '插入成功'
















