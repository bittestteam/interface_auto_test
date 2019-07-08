#coding=utf-8
import configparser
import redis
import pymysql

class publicMethod:

    # 获取redis连接
    # db为库几
    @staticmethod
    def get_redis(db):
        config= configparser.ConfigParser()
        config.read("config.ini")
        host = config['Redis']['host']
        port = config['Redis']['port']
        password = config['Redis']['password']
        r = redis.Redis(host=host, port=port, password=password, db=db)
        return r

    # 操作redis
    # db 为库几、method为操作方法、paramMap为参数
    @staticmethod
    def operate_redis(db,method,paramMap):
        r = publicMethod.get_redis(db)
        #method:1为新增或者修改，2为查询
        if method==1:
            for (key,value) in paramMap.items():
                print(key,value)
                r.set(key, value)
        elif method==2:
            for key in paramMap.keys():
                paramMap[key]=r.get(key)
        return paramMap

    @staticmethod
    def deal_url(paramMap):
        param = ""
        if paramMap!="":
            param="?"
            for key in paramMap:
                if paramMap[key] != "":
                    param = param + key + "=" + paramMap[key] + "&"
            param=param[:len(param) - 1]
        return param

    # 获取mysql连接
    @staticmethod
    def get_mysql():
        config= configparser.ConfigParser()
        config.read("config.ini")
        host = config['Mysql']['host']
        port = int(config['Mysql']['port'])
        user = config['Mysql']['user']
        password = config['Mysql']['password']
        database = config['Mysql']['database']
        charset = config['Mysql']['charset']
        conn = pymysql.connect(host=host, port=port, password=password, user=user,database=database,charset=charset)
        return conn

    # 增删改查
    # method=1 查询
    # method=2 增、删、改
    @staticmethod
    def operate_mysql(method, sql, params):

        try:
            conn = publicMethod.get_mysql()
            print (conn)
            curs =conn.cursor()
            print(curs)
            if method==1:
                print(sql)
                curs.execute(sql,params)
                result = curs.fetchall()
                print("查询成功")
                print (result)
                return result

            elif method==2:
                curs.execute(sql, params)
                conn.commit()
                print("更新成功")
                return True
            else:
                print("你输入的method类型不正确,1标识查询，2表示增删改")
        except:
            if method == 1:
                print('find出现错误')
            elif method == 2:
                print('cud出现错误')
                conn.rollback()
            conn.close()
            return False




