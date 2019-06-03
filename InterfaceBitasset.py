#coding=utf-8
import json


class InterfaceBitasset:
    def __init__(self,http):
        self.http = http

    def login(self,dataMap):
        path="/login"
        dataJson={}
        afsRequest={}
        afsRequest["scene"]=  "string"
        afsRequest["sessionId"] =  "string"
        afsRequest["sig"] =  "string"
        afsRequest["token"] =  "string"
        dataJson["afsRequest"]=afsRequest
        dataJson["areacode"] = ""
        dataJson["ip"] = ""
        dataJson["loginName"] = dataMap["loginName"]
        dataJson["passWord"] = dataMap["passWord"]
        return self.http.post(path,json.dumps(dataJson))

    def userInfo(self):
        path="/users/userInfo"
        return self.http.get(path)

    def backLogin(self,dataMap):
        path="/login"
        dataJson={}
        dataJson["password"] = dataMap["password"]
        dataJson["username"] = dataMap["username"]
        return self.http.post(path,json.dumps(dataJson),flag=1)







