class ParseCustomInfo(object):
    def InsertSql(self,datas):
        try:
            instance_name = datas['instanceName']
            instance_ip = datas['instanceIp']
            instance_port = datas['instancePort']
            instance_user = datas['instanceUser']
            instance_passwd = datas['instancePasswd']
            mysql = "insert into instance_info(instance_name,instance_ip_addr,instance_db_port,instance_user_name,instance_passwd) values('{0}','{1}','{2}','{3}','{4}')".format(
                    instance_name,instance_ip, instance_port,instance_user, instance_passwd)
        except Exception as e:
            return str(e)
        return mysql
    # 查询实例名
    def QuerySql(self):
        mysql = "select instance_name,instance_id from instance_info where isvalid = 1"
        return mysql
    # 查询所有实例信息
    def QueryAllSql(self):
        mysql = "select * from instance_info where isvalid = 1"
        return mysql

    def UpdateSql(self,instanceInfo_list):
        try:
            instance_name = instanceInfo_list['instanceName']
            instance_ip = instanceInfo_list['instanceIp']
            instance_port  = instanceInfo_list['instancePort']
            instance_user = instanceInfo_list['instanceUser']
            instance_passwd = instanceInfo_list['instancePasswd']
            instance_id = instanceInfo_list['instanceId']
            if instanceInfo_list['instanceIsinsertdb']=='否':
                instance_ISture = 0
            elif instanceInfo_list['instanceIsinsertdb']=='是':
                instance_ISture = 1
            mysql = "update instance_info set instance_name='{0}',instance_ip_addr='{1}',instance_db_port='{2}',instance_user_name='{3}',instance_passwd='{4}',isvalid={5} where instance_id={6}".format(
                    instance_name,instance_ip, instance_port,instance_user, instance_passwd,instance_ISture,instance_id)
        except Exception as e:
            return str(e)
        return mysql
    def DeleteSql(self,data):
        mysql = "update instance_info set isvalid={0} where instance_id={1}".format(0,data)
        return mysql