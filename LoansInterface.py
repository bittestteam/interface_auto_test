####接口说明：
# 如果是后台的请求，host不同，现在常规的是通过后台的路径中有gateway自行取host,
# 如果后台管理的接口中没有gateway，例如后台管理的登陆，就在调用post方法的时候添加flag=1
# 例如：post(path,json.dumps(dataJson),flag=1)


#coding=utf-8
import json



class LoansInterface:
    def __init__(self,http):
        self.http = http

#####前台的接口

    #借款广告操作
    #针对已经生成的广告的操作，例如修改
    def LoansAdvertOperation(self,dataMap):
        path="/proxy/portal/loans/advert/operation"
        dataJson={}
        dataJson["beginTime"] =  dataMap["beginTime"]
        dataJson["borrowCurrency"] = dataMap["borrowCurrency"]
        dataJson["borrowCycle"] = dataMap["borrowCycle"]
        dataJson["borrowMoney"] = dataMap["borrowMoney"]
        dataJson["dailyRate"] = dataMap["dailyRate"]
        dataJson["endTime"] = dataMap["endTime"]
        dataJson["pledgeCurrency"] = dataMap["pledgeCurrency"]
        dataJson["pledgeRatio"] = dataMap["pledgeRatio"]
        return self.http.post(path,json.dumps(dataJson))

    #获取广告基础参数
    def LoansAdvertParams(self,paramMap=""):
        path="/proxy/portal/loans/advert/params"
        return self.http.get(path,paramMap)

    #借款广告列表
    # 我的广告列表需要添加path：status Available values : ALL, FINISH
    #参数：page页数，size每页条数
    def LoansAdvertRecords(self,status="",paramMap=""):
        path = "/proxy/portal/loans/advert/records"
        if status!="":
            path = path+"/"+status
        return self.http.get(path, paramMap)

   #发布借贷广告
    def LoansAdvertRelease(self,dataMap):
        path="/proxy/portal/loans/advert/release"
        dataJson={}
        dataJson["beginTime"] =  dataMap["beginTime"]
        dataJson["borrowCurrency"] = dataMap["borrowCurrency"]
        dataJson["borrowCycle"] = dataMap["borrowCycle"]
        dataJson["borrowMoney"] = dataMap["borrowMoney"]
        dataJson["dailyRate"] = dataMap["dailyRate"]
        dataJson["endTime"] = dataMap["endTime"]
        dataJson["pledgeCurrency"] = dataMap["pledgeCurrency"]
        dataJson["pledgeRatio"] = dataMap["pledgeRatio"]
        return self.http.post(path,json.dumps(dataJson))

    # 平仓
    def LoansCloseOut(self, dataMap):
        path = "/proxy/portal/loans/close/out"
        dataJson = {}
        dataJson["orderNo"] = dataMap["orderNo"]
        return self.http.post(path, json.dumps(dataJson))

    #质押借贷数据统计
    def LoansDataStatistics(self,paramMap=""):
        path = "/proxy/portal/loans/data/statistics"
        return self.http.get(path, paramMap)

    # 出借
    def LoansInvestment(self, dataMap):
        path = "/portal/loans/investment"
        dataJson = {}
        dataJson["orderNo"] = dataMap["orderNo"]
        return self.http.post(path, json.dumps(dataJson))

    # 补仓
    #参数：orderNo订单号，amount补充数量
    def LoansLoansMarginCall(self, dataMap):
        path = "/portal/loans/margin/call"
        dataJson = {}
        dataJson["orderNo"] = dataMap["orderNo"]
        dataJson["amount"] = dataMap["amount"]
        return self.http.post(path, json.dumps(dataJson))

    # 补仓列表
    #path：orderNo 订单号
    # 参数：page页数，size每页条数
    def LoansMarginCallRecords(self, orderNo="",paramMap=""):
        path = "/portal/loans/margin/call/records/" + orderNo
        return self.http.get(path, paramMap)

    #我的质押借贷资产
    def LoansOwnerAsset(self,paramMap=""):
        path = "/portal/loans/owner/asset"
        return self.http.get(path, paramMap)

    #我的投资列表
    # 参数：page页数，size每页条数
    def LoansOwnerInvestmentRecords(self,paramMap=""):
        path = "/portal/loans/owner/investment/records"
        return self.http.get(path, paramMap)

    #我的贷款列表
    # 参数：page页数，size每页条数
    def LoansOwnerLoanRecords(self,paramMap=""):
        path = "/portal/loans/owner/loan/records"
        return self.http.get(path, paramMap)

    #质押借贷订单列表
    # 参数：borrow借款币种，broower借款人,lenders出借人，pledge质押物，page页数，size每页条数
    def LoansOwnerLoanRecords(self,paramMap=""):
        path = "/portal/loans/owner/loan/records"
        return self.http.get(path, paramMap)

    #还款
    #参数：orderNo订单号
    def LoansRepayment(self,dataMap=""):
        path = "/portal/loans/repayment"
        dataJson = {}
        dataJson["orderNo"] = dataMap["orderNo"]
        return self.http.post(path, json.dumps(dataJson))

#####后台管理接口

    #新增借出币种
    #参数：currencyId 币种ID，minLimit最小借款限额
    def LoansSettingsBorrowSet(self,dataMap=""):
        path = "/gateway/loans/settings/borrow"
        dataJson = {}
        dataJson["currencyId"] = dataMap["currencyId"]
        dataJson["minLimit"] = dataMap["minLimit"]
        return self.http.post(path, json.dumps(dataJson))

    #借出币种查询
    def LoansOwnerLoanRecordsGet(self,paramMap=""):
        path = "/gateway/loans/settings/borrow"
        return self.http.get(path, paramMap)

    #删除借出币种
    #path:id 编号
    def LoansSettingsBorrowDelete(self,id,dataMap=""):
        path = "/gateway/loans/settings/borrow/"+id
        return self.http.delete(path)

    #新增借款期限
    #参数：days 新增天数
    def LoansSettingsBorrowCycleSet(self,dataMap=""):
        path = "/gateway/loans/settings/borrow/cycle"
        dataJson = {}
        dataJson["days"] = dataMap["days"]
        return self.http.post(path, json.dumps(dataJson))

    #借款期限查询
    def LoansSettingsBorrowCycleGet(self,paramMap=""):
        path = "/gateway/loans/settings/borrow/cycle"
        return self.http.get(path, paramMap)

    #删除借款期限
    #path:id 编号
    def LoansSettingsBorrowCycleDelete(self,id,dataMap=""):
        path = "/gateway/loans/settings/borrow/cycle/"+id
        return self.http.delete(path)

    #逾期参数查询
    def LoansSettingsOverdue(self,paramMap=""):
        path = "/gateway/loans/settings/overdue"
        return self.http.get(path, paramMap)

    #逾期参数历史记录查询
    # 参数：page页数，size每页条数
    def LoansSettingsOverdueRecords(self,paramMap=""):
        path = "/gateway/loans/settings/overdue/records"
        return self.http.get(path, paramMap)

    # 逾期参数编辑
    # 参数：days 逾期期限
    # effectTime 生效时间
    # overdueInterestRate 逾期罚息率
    # overdueServiceRate 逾期服务费率
    def  LoansSettingsOverdueRenewal(self, dataMap=""):
        path = "/gateway/loans/settings/overdue/renewal"
        dataJson = {}
        dataJson["days"] = dataMap["days"]
        dataJson["effectTime"] = dataMap["effectTime"]
        dataJson["overdueInterestRate"] = dataMap["overdueInterestRate"]
        dataJson["overdueServiceRate"] = dataMap["overdueServiceRate"]
        return self.http.post(path, json.dumps(dataJson))

    # 新增质押物
    # 参数：advertWarnRatio 广告预警线
    # closeOutRatio 质押率平仓线
    # currencyId 质押物币种ID
    # effectTime 生效时间
    # initMaxRatio 初始最高质押率
    # serviceRatio 服务费率
    # warnRatio 质押率预警线
    def  LoansSettingsPledge(self, dataMap=""):
        path = "/gateway/loans/settings/pledge"
        dataJson = {}
        dataJson["advertWarnRatio"] = dataMap["advertWarnRatio"]
        dataJson["closeOutRatio"] = dataMap["closeOutRatio"]
        dataJson["currencyId"] = dataMap["currencyId"]
        dataJson["effectTime"] = dataMap["effectTime"]
        dataJson["initMaxRatio"] = dataMap["initMaxRatio"]
        dataJson["serviceRatio"] = dataMap["serviceRatio"]
        dataJson["warnRatio"] = dataMap["warnRatio"]
        return self.http.post(path, json.dumps(dataJson))

    #质押物列表查询
    # 参数：page页数，size每页条数
    def LoansSettingsPledgeRecords(self,paramMap=""):
        path = "/gateway/loans/settings/pledge/records"
        return self.http.get(path, paramMap)

    # 新增质押物
    # 参数：advertWarnRatio 广告预警线
    # closeOutRatio 质押率平仓线
    # currencyId 质押物币种ID
    # effectTime 生效时间
    # initMaxRatio 初始最高质押率
    # serviceRatio 服务费率
    # warnRatio 质押率预警线
    def  LoansSettingsPledgeRenewal(self, dataMap=""):
        path = "/gateway/loans/settings/pledge/renewal"
        dataJson = {}
        dataJson["advertWarnRatio"] = dataMap["advertWarnRatio"]
        dataJson["closeOutRatio"] = dataMap["closeOutRatio"]
        dataJson["currencyId"] = dataMap["currencyId"]
        dataJson["effectTime"] = dataMap["effectTime"]
        dataJson["initMaxRatio"] = dataMap["initMaxRatio"]
        dataJson["serviceRatio"] = dataMap["serviceRatio"]
        dataJson["warnRatio"] = dataMap["warnRatio"]
        return self.http.post(path, json.dumps(dataJson))

    #质押物参数历史列表查询
    # 参数：page页数，size每页条数
    def LoansSettingsPledgeHistoryRecords(self,currencyId,paramMap=""):
        path = "/gateway/loans/settings/pledge/"+currencyId+"/history/records"
        return self.http.get(path, paramMap)

    # 质押物详情查询
    # 参数：page页数，size每页条数
    def LoansSettingsPledgeDetail(self,currency,paramMap=""):
        path = "/gateway/loans/settings/pledge/"+currency
        return self.http.get(path, paramMap)