
class BackupAndRestore(object):
    def __init__(self,backup_list=[]):
        self.BKMode_dict = {'back_all':0,'back_diff':1,'back_log':2}
        self.RSOper_dict = {'recovery':0,'norecovery':1}
        self.OperMode_dict = {'处理孤立用户': 0, '新建用户授权': 1}
        self.backup_list = backup_list
    # 备份数据库
    def backup(self):
        db_name_str = ''
        OperType = 'BK'
        if self.backup_list != []:
            for db_name in self.backup_list['selectData']:
                db_name_str += db_name + ','
            BKFileUrl = self.backup_list['back_path']
            BKMode = self.BKMode_dict[self.backup_list['back_type']]
            BKDBKey = self.backup_list['KEY']
            sqlserver = r"exec BR.prBKandRestoreDBAll @DatabaseNames = N'{0}',@BKFileUrl = N'{1}',@BKDBKey = N'{2}',@OperType = N'{3}',@BKMode = {4}".format(
                db_name_str,BKFileUrl, BKDBKey,OperType, BKMode).encode("utf8")
            return sqlserver
        else:
            msg = '未获取到参数'
            return msg
    # 执行还原存储过程
    def restore(self):
        db_name_str = ''
        OperType = 'RS'
        if self.backup_list != []:
            for db_name in self.backup_list['selectData']:
                db_name_str += db_name + ','
            BKDBKey = self.backup_list['BKDBkey']
            BKMode = self.BKMode_dict[self.backup_list['back_type']]
            RSOper = self.RSOper_dict[self.backup_list['restore_type']]
            DBFileUrl = self.backup_list['datafile_path']
            LogFileUrl = self.backup_list['logfile_path']
            RSFileUrl = self.backup_list['backfile_path']
            sqlserver = r"exec BR.prBKandRestoreDBAll @DatabaseNames = N'{0}',@BKDBKey = N'{1}',@OperType = N'{2}',@RSMode={3},@RSOper= {4},@DBFileUrl='{5}',@LogFileUrl= N'{6}',@RSFileUrl=N'{7}'".format(
                db_name_str,BKDBKey,OperType, BKMode, RSOper,DBFileUrl,LogFileUrl,RSFileUrl)
            return sqlserver
        else:
            msg = '未获取到参数'
            return msg
    # 执行用户处理存储过程
    def user(self):
        db_name_str = ''
        OperType = 'CU'
        if self.backup_list != []:
            for db_name in self.backup_list['selectData']:
                db_name_str += db_name + ','
            sqlserver = r""
            return sqlserver
        else:
            msg = '未获取到参数'
            return msg
    # 插入状态表
    def BackUpStartSql(self,backup_list,data):
        mysql = "INSERT INTO operating(`operationName`,`operationType`,`db_name`,`instance_id`,`executiveDescribed`,`executingState`) VALUE('{0}','{1}','{2}',{3},'{4}',{5})".format(data['operationName'],data['operationType'],data['db_name'],data['instance_id'],data['executiveDescribed'],data['executingState'])
        return mysql
    def BackUpEndSql(self,data):
        mysql = "INSERT INTO operating(`operationName`,`operationType`,`db_name`,`instance_id`,`executiveDescribed`,`executingState`) VALUE('{0}','{1}','{2}',{3},'{4}'.{5})".format(data['operationName'],data['operationType'],data['db_name'],data['instance_id'],data['executiveDescribed'],data['executingState'])
        return mysql
    def RestoreStatusSql(self,data):
        mysql = "INSERT INTO operating(`operationName`,`operationType`,`db_name`,`instance_id`,`executiveDescribed`,`executingState`) VALUE('backup','全备',572,84,'备份成功',0)"
        return mysql

    def CUStatusSql(self,data):
        mysql = "INSERT INTO operating(`operationName`,`operationType`,`db_name`,`instance_id`,`executiveDescribed`,`executingState`) VALUE('backup','全备',572,84,'备份成功',0)"
        return mysql