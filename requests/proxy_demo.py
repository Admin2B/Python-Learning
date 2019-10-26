import requests,socket,socks
proxies={'http':'http://127.0.0.1:1080/pac?auth=swiiSEYO3cle17SNiuFe&t=201907280812555596',}
url='https://www.facebook.com'
#socks.set_default_proxy(socks.SOCKS5,"127.0.0.1",1080)
#socket.socket=socks.socksocket
response=requests.get(url,proxies=proxies)
print(response.status_code)