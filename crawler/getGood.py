# -*- coding: utf-8 -*-
import httplib
import urllib
import fileinput

url = "http://media.jd.com/gotoadv/goods"

conn = httplib.HTTPConnection('media.jd.com',80)

header = {"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
				   "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36",
				   "X-Requested-With":"XMLHttpRequest",
				   "Accept":"*/*",
				   "Connection":"keep-alive",
				   "Referer":"http://media.jd.com/index/overview",
				   "Upgrade-Insecure-Requests":1,
				   "Cookie":"thor=DA6124B09FDE296121C48480BA88E7C1FF6F9069424B344715E9E6ACF0A52116AD8DB98487554195FBEF0D8F9ED5C6A187EE13DB40520BFE7DA0F3AAEDB94B539C925C801BD25AEFE159D5558A42E21EDEC82F7701BC74A6DB334EAECF49AF1148CF654BECC6B27781AFACE6711A4283D949DE9FA77B17A462BA61E5EF13F998CAA647B54173B45BD2FC915003DD3144"
		}
conn.request("GET","/gotoadv/goods","",header);



res = conn.getresponse()

data =  res.read()

print data