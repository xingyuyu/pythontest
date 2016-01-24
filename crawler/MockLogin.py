# -*- coding: utf-8 -*-
import urllib2
import urllib
import random
from HTMLParser import HTMLParser
import httplib
class MockLogin:
	loginName = '18510154719'
	loginPass = 'yxy357159!'
	def getLoginPage (self) :
		url = "http://passport.jd.com/common/loginPage?from=media&ReturnUrl=http%3A%2F%2Fmedia.jd.com%2Findex%2Foverview"
		fp = urllib2.urlopen(url)
		data = fp.read()
		return data
	def getEid (self) :
		return '8fa5ec6cb99c427b8ec9c77252b68bc71078046231'
	def getFp(self):
		return 'ad7cbcec447035efad9919128244f42a'
	def login(self):
		objParse = LoginPageParse()
		objParse.feed(self.getLoginPage())
		loginMap = objParse.paramList
		#print loginMap
		url = 'passport.jd.com'
		loginMap['fp'] = self.getFp()
		loginMap['loginname'] = self.loginName
		loginMap['eid'] = self.getEid()
		loginMap['loginpwd'] = self.loginPass
		loginMap['nloginpwd'] = self.loginPass
		loginMap['machineNet'] = ""
		loginMap['machineCpu'] = ""
		loginMap['machineDisk'] = ""
		loginMap['authcode'] = ""
		del loginMap["chkRememberMe"]
		print loginMap
		reqParam = urllib.urlencode(loginMap)
		path = '/common/loginService?nr=1&uuid='+loginMap['uuid']+'&from=media&ReturnUrl=http%3A%2F%2Fmedia.jd.com%2Findex%2Foverview&r='+str(random.random())
		conn =  httplib.HTTPConnection(url,port=80,timeout=30)
		header = {"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
				   "Cookie":"mp=18510154719; ol=1; alc=KfxLXm6XciDquMdt9eqwhA==; _t=d31KMG8/g21wS08iZUhqc8bJpYuCfRgQLnV37BsGYxg=; __jda=95931165.1367332206.1453248200.1453248200.1453248200.1; __jdb=95931165.1.1367332206|1.1453248200; __jdc=95931165; __jdv=95931165|direct|-|none|-; __jdu=1367332206; e_png=8fa5ec6cb99c427b8ec9c77252b68bc71078046231; e_etag=8fa5ec6cb99c427b8ec9c77252b68bc71078046231; 3AB9D23F7A4B3C9B=8fa5ec6cb99c427b8ec9c77252b68bc71078046231",
				   "Referer":"http://passport.jd.com/common/loginPage?from=media&ReturnUrl=http%3A%2F%2Fmedia.jd.com%2Findex%2Foverview",
				   "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36",
				   "X-Requested-With":"XMLHttpRequest",
				   "Host":"passport.jd.com",
				   "Origin":"http://passport.jd.com",
				   "Accept":"*/*",
				   "Accept-Encoding":"gzip, deflate",
				   "Connection":"keep-alive",
				   "Content-Length":"251",
		}
		#urlReq = url+path
		#print urlReq
		#print header 
		#print path
		print reqParam
		conn.request("POST",path,reqParam,header)
		res = conn.getresponse()
		print res.getheaders()
		print res.read()

	pass
pass


class LoginPageParse(HTMLParser):
	paramList = {}
	def __init__(self):
		HTMLParser.__init__(self)
	pass
	def handle_starttag(self,tag,attrs):
		if tag =='input':
			isCatch = 0
			paramKey = ''
			myMap = {}
			for touple in attrs:
				if touple[0] == 'name':
					isCatch = 1
					paramKey = touple[1]
				elif isCatch == 1 and myMap.get(paramKey) == None :
					myMap = {paramKey:touple[1]};
					isCatch = 0
					self.paramList[paramKey] = touple[1]
					#return self.paramList
					pass
				pass
		pass
	def handle_endtag(self,tag):
		pass
	def handle_data(self,data):
		pass

pass
	

	
		

objMockLogin = MockLogin()

html =  objMockLogin.getLoginPage()
objParser = LoginPageParse()
objMockLogin.login()