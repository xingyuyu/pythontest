# -*- coding: utf-8 -*-
import httplib
import urllib
import fileinput
import string
import json
import sys
from bs4 import BeautifulSoup
url = "http://media.jd.com/gotoadv/goods"

conn = httplib.HTTPConnection('media.jd.com',80)

header = {"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
				   "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36",
				   "X-Requested-With":"XMLHttpRequest",
				   "Accept":"*/*",
				   "Connection":"keep-alive",
				   "Referer":"http://media.jd.com/index/overview",
				   "Upgrade-Insecure-Requests":1,
				   "Cookie":"thor=E4F35373FF306DF9E2DB21A01E6C1D9FF4F7AADFFEB61AE1E8E2AB3B4D0CB478805AE90BDCB850EE79FE3D5016744643DB006CB76E5A10D42433B4AD8C833DE780CCA2E9CA57FFB6FB32A858088171BE5FB0D06A6776B8558EE4248C9B7BC5EFA94348E24D56D634C7F4782BB6C09E127D293CC3D7BF9D916611E1EC060528F97E5D5FD12940558A01009BFD388FCC5A"
				   }

# param = {
# 	"pageIndex":,
# 	 "pageSize":10,
# 	# "category1":12218,
# 	 #"condition":1
# }
# strParam = urllib.urlencode(param)

def getPrometeUrl(shopInfo,paramList):
	reqParam = {}
	# reqParam["logType"] = 1
	# reqParam["logPromotionType"] = 1
	# reqParam["logTitle"] = shopInfo["name"]
	# reqParam["logUnitPrice"] = shopInfo["account"]
	# reqParam["logSaler"] = 1
	# reqParam["logCommissionLock"] = 0
	# reqParam["logPromotionStartTime"] = shopInfo["startTime"]
	# reqParam["logPromotionEndTIme"] = shopInfo["endTime"]
	# reqParam["imgUrl"] = shopInfo["imgUrl"]
	# reqParam["logCommissionRate"] = shopInfo["wiseRate"]
	reqParam["siteName"] = "微博"
	reqParam["materialType"] = 1
	reqParam["materialId"] = paramList[0]
	reqParam["positionId"] = 385773491
	reqParam["sizeType"] = 2
	reqParam["height"] = 0
	reqParam["width"] = 0
	reqParam["wareUrl"] = paramList[2]
	reqParam["adOwner"] = paramList[3]
	reqParam["popId"] = ""
	reqParam["CPType"] = "CPS"
	reqParam["adtType"] = 32
	reqParam["channel"] = "WL"
	reqParam["unionAppId"] = -1
	reqParam["unionMediaId"] = 5137
	reqParam["unionWebId"] = -1
	reqParam["type"] = 1
	reqParam["spaceName"] = 385773491
	reqParam["positionName"] = "test1"
	#print reqParam
	strReqParam = urllib.urlencode(reqParam)
	#print strReqParam
	header = {"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
				   "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36",
				   "X-Requested-With":"XMLHttpRequest",
				   "Accept":"*/*",
				   "Connection":"keep-alive",
				   "Referer":"http://media.jd.com/gotoadv/goods",
				   "Upgrade-Insecure-Requests":1,
				   "Cookie":"thor=E4F35373FF306DF9E2DB21A01E6C1D9FF4F7AADFFEB61AE1E8E2AB3B4D0CB478805AE90BDCB850EE79FE3D5016744643DB006CB76E5A10D42433B4AD8C833DE780CCA2E9CA57FFB6FB32A858088171BE5FB0D06A6776B8558EE4248C9B7BC5EFA94348E24D56D634C7F4782BB6C09E127D293CC3D7BF9D916611E1EC060528F97E5D5FD12940558A01009BFD388FCC5A"
				   }
	conn =  httplib.HTTPConnection("media.jd.com") 
	conn.request("POST","/gotoadv/getCustomCode/1",strReqParam,header)
	res = conn.getresponse()
	strRes =  res.read()
	mapRes = json.loads(strRes)
	return mapRes["shotCode"];
	#print res.status
	#sys.exit()
	pass

conn.request("GET","/gotoadv/goods?category1=&pageIndex=&condition=&pageSize=10",'',header);
#shopInfo = [{"name":"","smallPic":"","bigPic":"","originalUrl":"","sellerName":"","account":"","pcRate":"","wiseRate":"","pcMoney":"","wiseMony","","startTime":"","endTime":""}]
res = conn.getresponse()
data =  res.read()
objHtml = BeautifulSoup(data,"html.parser");

tdSet = objHtml.find_all("td");
i = -1
dataList = []
shopInfo = {}
for tdObj in tdSet:
	i = i+1
	if (i<8) :
		continue
	elif (i % 8 ==0):
		for child in tdObj.children:
			if (child.name == 'img'):
				src = child['src']
				#print child.contents[1].contents[3].contents[1]['href']
				shopInfo['imgUrl'] = src
				shopInfo['jdLink'] = child.contents[1].contents[1].contents[0]['href']
				shopInfo['name'] = child.contents[1].contents[1].contents[0].string
				###越界检查
				#shopInfo['sellerName'] = child.contents[1].contents[3].contents[1].contents[2]
			pass
	elif (i % 8 == 1) :
		shopInfo['account'] = tdObj.string.strip()
		pass
	elif (i % 8 == 2) :
		strPcRate = tdObj.contents[0].strip()
		shopInfo['pcRate'] = strPcRate.split(" ")[1]
		strWiseRate = tdObj.contents[2].strip()
		shopInfo['wiseRate'] = strWiseRate.split(" ")[1]
		pass
	elif (i % 8 == 3):
		strPcRate = tdObj.contents[0].strip()
		shopInfo['pcMoney'] = strPcRate.split(" ")[1]
		strWiseRate = tdObj.contents[2].strip()
		shopInfo['wiseMony'] = strWiseRate.split(" ")[1]
		pass
	elif (i % 8 == 4) :
		shopInfo['orderCount'] =  tdObj.string.strip()
		pass
	elif (i % 8 == 5) :
		shopInfo['orderAcountCount'] =  tdObj.string.strip()
		pass
	elif (i % 8 == 6) :
		shopInfo['startTime'] = tdObj.contents[1].contents[0].strip()
		shopInfo['endTime'] = tdObj.contents[1].contents[1].contents[2].strip()
		pass
	elif (i % 8 == 7) :
		param =  tdObj.contents[1]['onclick'][33:].lstrip("(").rstrip(")")
		paramList = param.split(",")
		shopInfo['bxUrl'] =  getPrometeUrl(shopInfo,paramList)
		pass
	else :
		break
	dataList.append(shopInfo)
pass

print dataList


