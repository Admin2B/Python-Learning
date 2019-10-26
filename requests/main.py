import json
import requests
from requests import exceptions
url='https://api.github.com'

def build_uri(endpoint):
    return '/'.join([url,endpoint])

def better_print(json_str):
    return json.dumps(json.loads(json_str),indent=4)

def request_method():
    response=requests.get(build_uri('users/Axxx'))
    print(better_print(response.text))

def params_request():
    response=requests.get(build_uri('users'),params={'since':'11'})
    print(better_print(response.text))
    print(response.request.headers)
    print(response.url)

def json_request():
    response=requests.patch(build_uri('user'),auth=('Axxxx','xxxxx'),
                            json={'bio':'Keep Coding.'})
    print(better_print(response.text))
    print(response.request.headers)
    print(response.request.body)
    print(response.status_code)

def timeout_request():
    try:
        response=requests.get(build_uri('user/emails'),timeout=10)
        response.raise_for_status()
    except exceptions.Timeout as e:
        print(e)
    except exceptions.HTTPError as e:
        print(e)
    else:
        print(response.text)
        print(response.status_code)

def hard_requests():
    from requests import Request,Session
    s=Session()
    headers={'User-Agent':'fake.1.2.3'}
    req=Request('GET',build_uri('user/emails'),auth=('Axxxb','xxxx'),
                headers=headers)
    prepped=req.prepare()
    print(prepped.body)
    print(prepped.headers)

    resp=s.send(prepped,timeout=5)
    print(resp.status_code)
    print(resp.request.headers)
    print(resp.text)


if __name__=='__main__':
    #request_method()
    #params_request()
    #json_request()
    #timeout_request()
    hard_requests()

