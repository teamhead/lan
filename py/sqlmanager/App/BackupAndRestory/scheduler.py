from App.BackupAndRestory.backupAndRestore import *
from App.BackupAndRestory.queryMssql import *
from App.BackupAndRestory.queryMysql import *
from concurrent.futures import ThreadPoolExecutor

class Sche(object):
    # 执行备份程序
    def backup(self,backup_list):
        if backup_list != {}:
            # 创建相关信息对象
            BKARS = BackupAndRestore(backup_list=backup_list)
            instance_name = backup_list['instance_id']
            instanceInfo = QueryInfo(instance_name)
            connInstance = instanceInfo.nameInstance()
            exec = ExeInfo(connInstance)
            sql = BKARS.backup()
            if sql == '未获取到参数':
                message = {'code': 1, 'msg': '参数传输失败'}
                return message
            else:
                backup_list['exe_result'] = 'backup'
                p = ThreadPoolExecutor(max_workers=2)
                p.submit(exec.exeSql,sql,backup_list)
                message = {'code': 0, 'msg': '已提交执行'}
                return message
        else:
            message = {'code': 1, 'msg': '参数传输失败'}
            return message
    # 生成还原语句程序
    def restore(self,restore_list):
        if restore_list != {}:
            BKARS = BackupAndRestore(backup_list=restore_list)
            instance_name = restore_list['instance_name']
            instanceInfo = QueryInfo(instance_name)
            connInstance = instanceInfo.nameInstance()
            exec = ExeInfo(connInstance)
            sql = BKARS.restore()
            if sql == '参数提交失败':
                message = {'code': 1, 'msg': '参数传输失败'}
                return message
            else:
                data = exec.exeSql(sql)
                if data == 'Statement not executed or executed statement has no resultset':
                    typeid = restore_list['back_type']
                    sql = exec.querySql(typeid,restore_list)
                    if sql == '':
                        message = {'code':1,'msg':'请输入正确的参数'}
                        return message
                    else:
                        message = {'code':0,'msg':sql}
                        return message
                else:
                    sql = data[0][1]
                    message = {'code': 0, 'msg': sql}
                    return message
        else:
            message = {'code':1,'msg':'参数传输失败'}
            return message
    # 生成用户操作语句
    def user(self,userInfo_list):
        if userInfo_list != {}:
            BKARS = BackupAndRestore(backup_list=userInfo_list)
            instance_name = userInfo_list['instance_name']
            instanceInfo = QueryInfo(instance_name)
            connInstance = instanceInfo.nameInstance()
            exec = ExeInfo(connInstance)
            sql = BKARS.restore()
            if sql == '参数提交失败':
                message = {'code': 1, 'msg': '参数传输失败'}
                return message
            else:
                data = exec.exeSql(sql)
                if data == 'Statement not executed or executed statement has no resultset':
                    sql = exec.queryUserSql(userInfo_list)
                    if sql == '':
                        message = {'code':1,'msg':'请输入正确的参数'}
                        return message
                    else:
                        message = {'code':0,'msg':sql}
                        return message
                else:
                    pass
        else:
            message = {'code':1,'msg':'参数传输失败'}
            return message
    # 执行语句
    def exe_sql(self,request_list):
        if request_list != {}:
            instance_name = request_list['target_instance']
            instanceInfo = QueryInfo(instance_name)
            connInstance = instanceInfo.nameInstance()
            exec = ExeInfo(connInstance)
            sql_list = request_list['modify_sql']
            for sql in sql_list:
                exec.exeSql(sql)
            message = {'code':0,'msg':'语句已提交'}
            return message
        else:
            message = {'code':1,'msg':'参数传输失败'}
            return message
    def switchID(self,db_name):
        pass
    def switchName(self,db_id):
        pass
    def insertLog(self):
        print('插入记录')

