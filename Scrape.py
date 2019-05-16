import requests
from bs4 import BeautifulSoup
import time
import urllib

count=0
total=0
err=0

file = open("FullList.csv", "r")
file2 = open("Output.txt","w")
file3 = open("error.txt", "w")

def func(url):
	global count, total, err
	total+=1
	#url='http://google.com'
	res = requests.get(url)
	#print (res.text)
	soup = BeautifulSoup(res.text, 'lxml')
	for i in soup.find_all('script'):
		if i.get('src')!=None:
			print ("src:", i.get('src'))
			if "mine" in i.get('src'):
				count+=1
def main():
	print ("in main")

	#url=[]

	for i in file.readlines():
		i=i.replace('\n','')
		print (i)
		func(i)
		print (count)

if __name__=='__main__':
    main()
