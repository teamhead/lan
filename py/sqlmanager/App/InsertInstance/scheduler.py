from App.InsertInstance.queryMysql import *
from App.InsertInstance.parseCustomInfo import *
import time
class Sche(object):
    # 插入实例信息
    def InsertInstance(self,datas):
        if datas:
            parse = ParseCustomInfo()
            sql = parse.InsertSql(datas)
            exeSql = QueryInfo()
            if sql == 0:
                message = {'code':1,'msg':'not find args'}
                return message
            else:
                datas = exeSql.exeSqlinsert(sql)
                return datas# 此处判断是否执行成功
        else:
            message = {'code':1,'msg':'not find args'}
            return message
    # 查询实例信息
    def queryInstance(self):
        parse = ParseCustomInfo()
        sql = parse.QuerySql()
        exeSql = QueryInfo()
        datas = exeSql.exeSql(sql)
        instance = []
        for instance_name in datas[0][1]:
            instanceinfo = {}
            instanceinfo['instance_name']=instance_name[0]
            instanceinfo['instance_id']=instance_name[1]
            instance.append(instanceinfo)
        message = {'code':0,'msg':instance}
        return message

    # 查询所有实例信息
    def queryAllInstance(self):
        parse = ParseCustomInfo()
        sql = parse.QueryAllSql()
        exeSql = QueryInfo()
        datas = exeSql.exeSql(sql)
        info = []
        for data in datas[0][1]:
            message = {}
            message['instanceId'] = data[5]
            message['instanceName'] = data[6]
            message['instanceIp'] = data[7]
            message['instancePort'] = data[8]
            message['instanceUser'] = data[9]
            message['instancePasswd'] = data[10]
            message['instanceCreateTime'] = int(time.mktime(data[3].timetuple()))
            if data[11] == 0:
                message['instanceIsinsertdb'] = '是'
            elif data[11] == 1:
                message['instanceIsinsertdb'] = '否'
            info.append(message)
        return info


    # 修改实例信息
    def updateInstance(self,instanceInfo_list):
        parse = ParseCustomInfo()
        sql = parse.UpdateSql(instanceInfo_list)
        exeSql = QueryInfo()
        datas = exeSql.exeSqlinsert(sql)
        return datas


    # 禁用实例信息
    def deleteInstance(self,data):
        parse = ParseCustomInfo()
        sql = parse.DeleteSql(data)
        exeSql = QueryInfo()
        datas = exeSql.exeSqlinsert(sql)
        return datas