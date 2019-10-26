import urllib
from urllib import request,parse
url_ip='http://httpbin.org/ip'
url_get='http://httpbin.org/get'

def use_simple_urllib():
    response=urllib.request.urlopen(url_ip)
    print('>>>>>Response Headers:')
    print(response.info())
    print('>>>>Response Body:')
    print(response.read().decode('utf-8'))

def use_params_urllib():
    #构建请求参数
    params=urllib.parse.urlencode({'param1':'hello','param2':'world'})
    print('Request Params:')
    print(params)

    #发送请求
    response=urllib.request.urlopen('?'.join([url_get,'%s'])%params)

    #处理响应
    print('>>>>>Response Headers:')
    print(response.info())
    print('>>>>Status Code:')
    print(response.getcode())
    print('>>>>Response Body:')
    print(response.read().decode('utf-8'))




if __name__=='__main__':
    print('>>>>use_simple_urllib')
    use_simple_urllib()
    print('')

    print('use_params_urllib:')
    use_params_urllib()
