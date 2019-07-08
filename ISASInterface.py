####接口说明：
# 如果是后台的请求，host不同，现在常规的是通过后台的路径中有gateway自行取host,
# 如果后台管理的接口中没有gateway，例如后台管理的登陆，就在调用post方法的时候添加flag=1
# 例如：post(path,json.dumps(dataJson),flag=1)


#coding=utf-8
import json



class ISASInterface:
    def __init__(self,http):
        self.http = http

#####前台的接口

    # 获取昨日收盘价
    # 参数：contractId   交易对id
    def GetYestodayLastPrice(self,paramMap=""):
        path="/gateway/activity/isas/getYestodayLastPrice"
        return self.http.get(path,paramMap)

    # 获取公振动奖励
    def GetRewardInfo(self,paramMap=""):
        path="/gateway/activity/isas/getRewardInfo"
        return self.http.get(path,paramMap)

####后台的接口

    # 新建规则
    # avgPosi 持仓要求
    # avgPrice 五日均价
    # awardPoolSource 额度来源url
    # prizePoolMount 奖池
    # sort 优先级
    def CreateIsasConfig(self,dataMap):
        path="/bg/activity/isas/createIsasConfig"
        dataJson={}
        dataJson["avgPosi"] =  dataMap["avgPosi"]
        dataJson["avgPrice"] = dataMap["avgPrice"]
        dataJson["awardPoolSource"] = dataMap["awardPoolSource"]
        dataJson["prizePoolMount"] = dataMap["prizePoolMount"]
        dataJson["sort"] = dataMap["sort"]
        return self.http.post(path,json.dumps(dataJson))

    # 删除共振配置
    #path:id 编号
    def DeleteConfig(self,id,dataMap=""):
        path = "/bg/activity/isas/deleteConfig/"+id
        return self.http.delete(path)

    # 查询数据来源用户资产
    # 参数：userId:用户id
    def FindUserSpotAsset(self,paramMap=""):
        path="/bg/activity/isas/findUserSpotAsset"
        return self.http.get(path,paramMap)

    # 获取共振奖励信息
    def GetBgRewardInfo(self,paramMap=""):
        path="/bg/activity/isas/getBgRewardInfo"
        return self.http.get(path,paramMap)

    # 获取价格信息
    def GetPriceInfo(self,paramMap=""):
        path="/bg/activity/isas/getPriceInfo"
        return self.http.get(path,paramMap)

    # 获取用户反振持仓表
    # 参数：
    # avgPosi：持仓数量
    # endTime：结束时间。13位毫秒数
    # startTime：开始时间。13位毫秒数
    # userId：用户id
    def GetUserPosi(self,paramMap=""):
        path="/bg/activity/isas/getUserPosi"
        return self.http.get(path,paramMap)

    # 发放奖励
    # url参数：id 主键id
    def Providereward(self,id):
        path="/bg/activity/isas/providereward/"+id
        return self.http.post(path)

    # 开启共振开关
    # url参数：flag： true(开)，false(关)
    def IASASwitch(self,dataMap):
        for d in dataMap:
            path = "/bg/activity/isas/switch/?flag="+dataMap["flag"]
            return self.http.post(path, dataMap)


    # 修改共振配置
    # avgPosi 平均持仓
    # avgPrice 持仓均价
    # awardPoolSource 奖励来源用户id
    # prizePoolMount 奖池金额
    # provideStatus  0未生效；1待启动；2已开启待发放；3已发放
    # sort 排序id
    def UpdateConfig(self,dataMap):
        path="/bg/activity/isas/updateConfig"
        dataJson={}
        dataJson["avgPosi"] =  dataMap["avgPosi"]
        dataJson["avgPrice"] = dataMap["avgPrice"]
        dataJson["awardPoolSource"] = dataMap["awardPoolSource"]
        dataJson["prizePoolMount"] = dataMap["provideStatus"]
        dataJson["provideStatus"] = dataMap["provideStatus"]
        dataJson["sort"] = dataMap["sort"]
        return self.http.post(path,json.dumps(dataJson))

    # 修改价格信息（实时生效）
    # highPrice string 今日最高价
    # lowPrice  string 今日最低价
    # yesLastPrice string 昨日收盘价
    def UpdatePrice(self,dataMap):
        path="/bg/activity/isas/updatePrice"
        dataJson={}
        dataJson["highPrice"] =  dataMap["highPrice"]
        dataJson["lowPrice"] = dataMap["lowPrice"]
        dataJson["yesLastPrice"] = dataMap["yesLastPrice"]
        return self.http.post(path,json.dumps(dataJson))

    # 进行资产快照（实时生效）
    def RecordAsset (self,a=""):
        path="/bg/activity/isas/recordAsset "
        return self.http.post(path)

    # 重置昨日收盘价
    def ResetClosePrice(self):
        path="/bg/activity/isas/resetClosePrice "
        return self.http.post(path)