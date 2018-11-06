from joblib import Parallel, delayed
import multiprocessing
from collections import Counter
import math
import time
import os
import urllib2
import urllib
#from genericparser import GenericParser
import cookielib
import re


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

file2 = open("hakunaMatata.txt", "w")
count=0
total=0
err=0
def func(url):
    global count
    global total, err
    total+=1
    url="https://"+url
    #print url

    req = urllib2.Request(url,headers=head)
    
    try:
        res =opener.open(req, timeout=1)
        resdata=res.read()
        # count+=1

    except:
        resdata=""

    #print resdata
    if resdata=="":
        err+=1
        #print url
    listof=[]

    listof = re.findall('<script src="(.*?)".*?>', resdata)

    #print listof
    #time.sleep(1)
    #print len(listof)

    for i in listof:
        #print i
        # if i=="https://minero.cc/lib/minero-miner.min.js":
        #     print "I mera ye hai" + i
        #     count+=1
        if "mine" in i or "coin" in i:
            file2.write(url+" -> "+i+"\n")
            count+=1
            print "Found"

    os.system("clear")

    print "total = " + str(total)
    print "error = " + str(err)


def main():
    print ("in main")
    global count
    #t1=time.time()
    file=open("FullList.csv","r")
    url=[]
    
    for i in file.readlines():
        url.append(i.replace("\n",""))
    
    file.close()

    num_cores = multiprocessing.cpu_count()
    print num_cores
    #results = Parallel(n_jobs=num_cores)(delayed(func)(i) for i in url)
    #url = ["github.com"]
    for i in url:
        func(i)
    print "count= " + str(count)
    


if __name__=='__main__':
	main()
