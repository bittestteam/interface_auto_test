#coding=utf-8
import os
import types

import requests
import time

from LoansInterface import LoansInterface
from httpConfig import *
import collections
import unittest
from publicMethod import *
from InterfaceBitasset import *
import HTMLTestRunner

from ddt import ddt, data


@ddt
class testInterface(unittest.TestCase):


    #必须使用@classmethod 装饰器,所有test运行前运行一次
    @classmethod
    def setUpClass(self):
        self.loginList={"loginName":"20182","passWord":"a123456"}
        self.http = httpConfig()
        self.interfaceBit=InterfaceBitasset(self.http)
        redisData={}
        redisData["ARGS_asfWebAppKey"]="{'extObject': ''}"
        publicMethod.operate_redis(0, 1,redisData)
        if self.loginList!=None:
            responseMap = self.interfaceBit.login(self.loginList)
            #print(responseMap)
            self.http.headers["Authorization"] = responseMap["data"]






    # 每个测试用例执行之前做操作
    def setUp(self):
        pass


    # 每个测试用例执行之后做操作
    def tearDown(self):
        pass

    # 必须使用 @ classmethod装饰器, 所有test运行完后运行一次
    @classmethod
    def tearDownClass(self):
         pass

    #下单接口测试
    @data([{"code":200,"floginname":"20182"}],
          [{"code":200,"floginname":"20182"}])
    def test_userInfo(self,value):
        response = self.interfaceBit.userInfo()
        responseMap=json.loads(response.text)
        #print(response.text)
        print(response.status_code)
        assert response.status_code==value[0]["code"]
        assert responseMap["floginname"] == value[0]["floginname"]




if __name__ == "__main__":

    # # 构造测试集
    #suite = Suite1()
    #suite=unittest.TestSuite()
    #suite.addTest(testInterface("test_userInfo"))
    # # # 执行测试
    filePath ='report/Report.html'       #确定生成报告的路径
    fp = open(filePath,'wb')
    #runner = HTMLTestRunner.HTMLTestReportCN(stream=fp, title=u'接口测试报告')
    #runner.run(suite)
    unittest.main(testRunner=HTMLTestRunner.HTMLTestReportCN(stream=fp, title=u'接口测试报告'))










