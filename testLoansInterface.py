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
        self.loginList = {"username": "楼珊", "password": "a123456"}
        self.http = httpConfig()
        self.interfaceBit=InterfaceBitasset(self.http)
        self.loansInterface=LoansInterface(self.http)
        if self.loginList!=None:
            responseMap = self.interfaceBit.backLogin(self.loginList)
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
    #参数：currencyId
    #      minLimit
    @data([{"in":{"currencyId": 1, "minLimit": 100},"out":{"code":"200","msg":"操作成功"}}],
          [{"in":{"currencyId": 2, "minLimit": 100.1},"out":{"code":"40010022","msg":"最小借款限额不合法"}}])
    def test_LoansSettingsBorrowSet(self,value):
        for v in value:
            response = self.loansInterface.LoansSettingsBorrowSet(v["in"])
            #responseMap = json.loads(response.text)
            print(response)
            self.assertEqual(response["code"],v["out"]["code"])
            self.assertEqual(response["msg"], v["out"]["msg"])
            time.sleep(3)




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










