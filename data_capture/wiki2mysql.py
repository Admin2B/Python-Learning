from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pymysql.cursors

resp=urlopen('https://en.wikipedia.org/wiki/Main_Page').read().decode('utf-8')
soup=BeautifulSoup(resp,'html.parser')
listUrls=soup.find_all('a',href=re.compile(r'^/wiki/'))

for url in listUrls:
    if not re.search('\.(jpg|JPG)$',url['href']):
        print(url.get_text(),'<----->','https://en.wikipedia.org'+url['href'])
        connection=pymysql.connect(host='localhost',user='root',password='root',db='wikiurl',charset='utf8mb4')
        try:
            #获取会话指针
            with connection.cursor() as cuosor:
                #创建sql
                sql='insert into `urls`(`urlname`,`urlhref`) values (%s,%s)'

                #执行sql语句
                cuosor.execute(sql,(url.get_text(),'https://en.wikipedia.org'+url['href']))
                #提交
                connection.commit()



        finally:
            connection.close()