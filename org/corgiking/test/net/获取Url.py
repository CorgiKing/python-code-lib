#coding=utf-8
import urllib
import re
import pymysql

str = "http://top.chinaz.com/hangye/"

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html
	
def getUrls(html):
	reg = r'<span class="col-gray">[a-zA-Z0-9.]*</span>'
	urlre = re.compile(reg)
	urllist = re.findall(urlre,html)
	
	urls=[]
	for i in urllist:
		j = i.split('>')[1].split('<')[0]
		urls.append(j)
	return urls

def getNextUrl(html):
	reg = r'<a href="[^>]*"> > </a>'
	urlre = re.compile(reg)
	url = re.findall(urlre,html)
	return str + url[0].split('"')[1]
	
def findUrls(html,num):
	allUrls = []
	allUrls.extend(getUrls(html))
	while len(allUrls) < num:
		url = getNextUrl(html)
		html = getHtml(url)
		allUrls.extend(getUrls(html))
		
	print (len(allUrls))
	return allUrls
	
def saveDb(urls,num):
	conn = pymysql.connect(host='192.168.4.170', port=3306, user='', passwd='', db='')
	cursor = conn.cursor()
	cursor.execute("truncate table t_ping_net")
	sql = "insert into t_ping_net(domain_name) values(%s)"
	i = 0
	while i < num:
		cursor.execute(sql,urls[i])
		i = i + 1
	conn.commit()
	cursor.close()
	conn.close()
	

html = getHtml(str + "index.html")
urls = findUrls(html,100)
for i in urls:
	print (i)
saveDb(urls,100)
	



	


input("Press <enter> exit!")
exit()

