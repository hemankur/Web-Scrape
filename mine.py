import urllib2
import urllib
#from genericparser import GenericParser
import cookielib
import re
import os

cookies = cookielib.CookieJar()
cookie_handler=urllib2.HTTPCookieProcessor(cookies)
redirect_handler=urllib2.HTTPRedirectHandler()

opener = urllib2.build_opener(redirect_handler,cookie_handler)

head={
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,/;q=0.8',
#'Accept-Encoding':'gzip, deflate, br',
'Accept-Language':'en-US,en;q=0.5',
'Connection':'keep-alive',
#'Host':'minero.cc',
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0'
}

url="https://minero.cc/"


req = urllib2.Request(url,headers=head)
res =opener.open(req)
resdata=res.read()

print resdata


listof = re.findall('<script src=(.*?) .*?>', resdata)

for i in listof:
	if i=='"https://minero.cc/lib/minero-miner.min.js"':
		print "Found"
	print i
