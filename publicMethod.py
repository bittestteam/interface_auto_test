#coding=utf-8
import configparser
import redis

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


