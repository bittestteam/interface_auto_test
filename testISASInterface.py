#coding=utf-8
import os
import types

import requests
import time

from ISASInterface import *
from httpConfig import *
import collections
import unittest
from publicMethod import *
from InterfaceBitasset import *
import HTMLTestRunner

from ddt import ddt, data


@ddt
class testISASInterface(unittest.TestCase):


    #必须使用@classmethod 装饰器,所有test运行前运行一次
    @classmethod
    def setUpClass(self):
        self.login_f = {"username": "楼珊", "password": "a123456"}
        self.login_b = {"username": "楼珊", "password": "a123456"}
        self.http = httpConfig()
        self.interfaceBit=InterfaceBitasset(self.http)
        self.iSASInterface=ISASInterface(self.http)
        responseMap = self.interfaceBit.backLogin(self.login_f)
        self.jessonid_f = responseMap["data"]
        responseMap = self.interfaceBit.backLogin(self.login_b)
        self.jessonid_b = responseMap["data"]



        #self.http.headers["Authorization"] =jessonid_f

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

    # # 新建规则接口测试
    # # avgPosi 持仓要求
    # # avgPrice 五日均价
    # # awardPoolSource 额度来源url
    # # prizePoolMount 奖池
    # # sort 优先级
    # #对应检查的数据库表 active_provide_config
    # @data([{"测试点":"正常新建","in":{"avgPosi":  1000.123, "avgPrice": 0.023, "awardPoolSource": 666666, "prizePoolMount": 10000.123,"sort": 1}, "out": {"code": "200", "msg":"操作成功"}}],
    #       [{"测试点":"正常新建","in": {"avgPosi": 1000000, "avgPrice": 123.123, "awardPoolSource": 666666, "prizePoolMount": 1000000,"sort": 1}, "out": {"code": "200", "msg": "操作成功"}}],
    #       [{"测试点":"5日均价待定","in": {"avgPosi": "", "avgPrice": 123.123, "awardPoolSource": 666666, "prizePoolMount": 1000000,"sort": 1}, "out": {"code": "200", "msg": "操作成功"}}],
    #       [{"测试点":"持仓要求待定","in": {"avgPosi": 1, "avgPrice": 123.123, "awardPoolSource": 666666, "prizePoolMount": "", "sort": 1},"out": {"code": "200", "msg": "操作成功"}}],
    #       [{"测试点": "5日均价待定后，额度来源也可以为空","in": {"avgPosi": 1, "avgPrice": 123.123, "awardPoolSource": "", "prizePoolMount": "", "sort": 1},"out": {"code": "200", "msg": "操作成功"}}],
    #       [{"测试点": "avgPrice为空验证","in": {"avgPosi": 1, "avgPrice": "", "awardPoolSource": 666666, "prizePoolMount": "", "sort": 1},"out": {"code": "500001", "msg": "5日均价参数非法"}}],
    #       [{"测试点": "sort为空验证","in": {"avgPosi": 1, "avgPrice": 123.123, "awardPoolSource": 666666, "prizePoolMount": "", "sort": ""},"out": {"code": "500001", "msg": "显示优先级参数非法"}}]
    #       )
    # def test_LoansSettingsBorrowSet(self,value):
    #     for v in value:
    #         print(v["测试点"])
    #         response = self.iSASInterface.CreateIsasConfig(v["in"])
    #         #responseMap = json.loads(response.text)
    #         print(response)
    #         self.assertEqual(response["code"],v["out"]["code"])
    #         self.assertEqual(response["msg"], v["out"]["msg"])
    #         time.sleep(2)

    # # 删除共振配置接口测试
    # #path:id 编号
    # @data([{"测试点": "正常删除","in": {"id":"1"}, "out": {"code": "200", "msg": "操作成功"}}],
    #       [{"测试点": "删除不存在的id", "in": {"id": "2"}, "out": {"code": "200", "msg": "操作成功"}}]
    #       )
    # def test_DeleteConfig(self,value):
    #     for v in value:
    #         print(v["测试点"])
    #         response = self.iSASInterface.DeleteConfig(v["in"]["id"])
    #         # responseMap = json.loads(response.text)
    #         print(response)
    #         self.assertEqual(response["code"], v["out"]["code"])
    #         self.assertEqual(response["msg"], v["out"]["msg"])
    #         time.sleep(2)

    # #  查询数据来源用户资产
    # # 参数：userId:用户id
    # @data([{"测试点": "正常查询","in": {"userId":"666722"}, "out": {"code": "200", "msg": "操作成功"}}],
    #       [{"测试点": "查询不存在的用户id", "in": {"userId": "666666"}, "out": {"code": "200", "msg": "操作成功"}}]
    #       )
    # def test_FindUserSpotAsset(self,value):
    #     for v in value:
    #         print(v["测试点"])
    #         response = self.iSASInterface.FindUserSpotAsset(v["in"])
    #         # responseMap = json.loads(response.text)
    #         print(response)
    #         self.assertEqual(response["code"], v["out"]["code"])
    #         self.assertEqual(response["msg"], v["out"]["msg"])
    #         time.sleep(2)

    # # 获取共振奖励信息
    # #返回data数据字段，返回所有状态不为4的数据
    # # {
    # #   "id": 1,                       主键id
    # #   "avgPrice": 0.5,               近五日均价
    # #   "avgPosi": 10,                 近五日持仓
    # #   "prizePoolMount": 100,         奖励金额
    # #   "createTime": 1560390885734,   创建时间
    # #   "sort": 2,                     排序id
    # #   "provideStatus": 1,              0未生效；1待启动；2已开启待发放；3已发放
    # #   "completionTime":1560390885734  达成奖励时间
    # #   "provideTime":1560390885734  发放时间
    # # }
    # @data([{"测试点": "正常查询","out": {"code": "200", "msg": "操作成功"}}]
    #       )
    # def test_GetBgRewardInfo(self,value):
    #     for v in value:
    #         print(v["测试点"])
    #         response = self.iSASInterface.GetBgRewardInfo()
    #         # responseMap = json.loads(response.text)
    #         print(response)
    #         self.assertEqual(response["code"], v["out"]["code"])
    #         self.assertEqual(response["msg"], v["out"]["msg"])
    #         time.sleep(2)

    # #  获取价格信息
    # #  返回data格式
    # #     "yesLastPrice": "0.5", 昨收价
    # #     "highPrice": "0.525", 最高价
    # #     "lowPrice": "0.475"  最低价
    # #  相关的数据库表`active_provide_price_record`
    # @data([{"测试点": "正常查询","out": {"code": "200", "msg": "操作成功"}}])
    # def test_GetPriceInfo(self,value):
    #     for v in value:
    #         print(v["测试点"])
    #         response = self.iSASInterface.GetPriceInfo()
    #         # responseMap = json.loads(response.text)
    #         print(response)
    #         self.assertEqual(response["code"], v["out"]["code"])
    #         self.assertEqual(response["msg"], v["out"]["msg"])
    #         time.sleep(2)

    # # 获取用户反振持仓表
    # # 参数：
    # # avgPosi：持仓数量
    # # endTime：结束时间。13位毫秒数
    # # startTime：开始时间。13位毫秒数
    # # userId：用户id
    # # 相关的数据库表 active_provide_asset_record
    # # 返回data:
    # # "currencyName": "ISAS", 币种名称
    # # "userId": 666722, 用户id
    # # "userName": "蔡邦超", 用户姓名
    # # "avgPosi": 8750 平均持仓
    # @data([{"测试点":"持仓数量查询","in":{"avgPosi": "", "startTime": "1560182400000", "endTime": "1560614399059", "userId": ""}, "out": {"code": "200", "msg": "操作成功"}}]
    #       [{"测试点":"用户id查询", "in": {"avgPosi":"" ,  "startTime": "", "endTime": "", "userId": "666722"}, "out": {"code": "200", "msg": "操作成功"}}],
    #       [{"测试点": "时间查询",  "in": {"avgPosi": "",   "startTime": "1560398400022", "endTime": "1560398400023", "userId": ""}, "out": {"code": "200", "msg": "操作成功"}}],
    #       [{"测试点": "组合测试1", "in": {"avgPosi": "9000", "startTime": "1560225600000", "endTime": "1560398400023", "userId": ""}, "out": {"code": "200", "msg": "操作成功"}}],
    #       [{"测试点": "组合测试2", "in": {"avgPosi": "8500", "startTime": "", "endTime": "", "userId": "666722"}, "out": {"code": "200", "msg": "操作成功"}}],
    #       [{"测试点": "组合测试3", "in": {"avgPosi": "", "startTime": "1560312000000", "endTime": "1560398400023", "userId": "666666"}, "out": {"code": "200", "msg": "操作成功"}}],
    #       [{"测试点": "组合测试4", "in": {"avgPosi": "8500", "startTime": "1560312000000", "endTime": "1560398400022", "userId": "666722"}, "out": {"code": "200", "msg": "操作成功"}}])
    # def test_GetUserPosi(self,value):
    #     for v in value:
    #         print(v["测试点"])
    #         response = self.iSASInterface.GetUserPosi(v["in"])
    #         # responseMap = json.loads(response.text)
    #         print(response)
    #         self.assertEqual(response["code"], v["out"]["code"])
    #         self.assertEqual(response["msg"], v["out"]["msg"])
    #         time.sleep(1)

    # # 发放奖励
    # # avgPosi 持仓要求
    # # avgPrice 五日均价
    # # awardPoolSource 额度来源url
    # # prizePoolMount 奖池
    # # sort 优先级
    # #对应检查的数据库表 active_provide_config
    # @data([{"测试点":"正常新建","in":{"id": "1"}, "out": {"code": "200", "msg":"操作成功"}}])
    # def test_Providereward(self,value):
    #     for v in value:
    #         print(v["测试点"])
    #         response = self.iSASInterface.Providereward(v["in"]["id"])
    #         #responseMap = json.loads(response.text)
    #         print(response)
    #         self.assertEqual(response["code"],v["out"]["code"])
    #         self.assertEqual(response["msg"], v["out"]["msg"])
    #         time.sleep(2)

    # # 开启共振开关
    # # url参数：flag： true(开)，false(关)
    # @data([{"测试点": "正常新建", "in": {"flag": "true"}, "out": {"code": "200", "msg":"操作成功"}}],
    #       [{"测试点": "正常新建", "in": {"flag": "false"}, "out": {"code": "200", "msg": "操作成功"}}])
    # def test_IASASwitch(self,value):
    #     for v in value:
    #         print(v["测试点"])
    #         response = self.iSASInterface.IASASwitch(v["in"])
    #         #responseMap = json.loads(response.text)
    #         print(response)
    #         self.assertEqual(response["code"],v["out"]["code"])
    #         self.assertEqual(response["msg"], v["out"]["msg"])
    #         time.sleep(2)

    # 进行资产快照
    def test_RecordAsset(self):
        self.http.headers["Authorization"] = self.jessonid_f
        response = self.iSASInterface.RecordAsset()
        self.http.headers["Authorization"] = self.jessonid_b

        # responseMap = json.loads(response.text)
        print(response)

    # # 进行资产快照
    # def test_ResetClosePrice(self):
    #     response = self.iSASInterface.RecordAsset()
    #     # responseMap = json.loads(response.text)
    #     print(response)



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










