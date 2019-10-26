
import re
import urllib
req=urllib.request.urlopen('https://www.imooc.com/course/list')
buf=req.read().decode('utf-8')
#print(buf)

listurl=re.findall(r'data-original=".+\.jpg',str(buf))
listurl=re.sub(r'data-original="','http:',str(listurl))

listurl = re.findall(r'http:.+?\.jpg',listurl)

print(type(listurl)) #str
print(listurl)


i=0
for url in listurl:
    f=open(str(i)+'.jpg','wb')
    req=urllib.request.urlopen(url)
    buf=req.read()
    f.write(buf)
    i+=1
    f.close()





