import requests
url_ip='http://httpbin.org/ip'
url_get='http://httpbin.org/get'

def use_simple_requests():
    response=requests.get(url_ip)
    print('>>>>>Response Headers:')
    print(response.headers)
    print('>>>>Response Body:')
    print(response.text)

def use_params_requests():
    #构建请求参数
    params={'param1':'hello','param2':'world'}
    #发送请求
    response=requests.get(url_get,params=params)

    #处理响应
    print('>>>>>Response Headers:')
    print(response.headers)
    print('>>>>Status Code:')
    print(response.status_code)
    print(response.reason)
    print('>>>>Response Body:')
    print(response.json())

if __name__=='__main__':
    print('>>>>use_simple_requests')
    use_simple_requests()

    print('use_params_requests:')
    use_params_requests()
