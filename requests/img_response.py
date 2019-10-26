import requests

def download_image():
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
    url='http://ku.90sjimg.com/element_origin_min_pic/01/54/84/385747392bd3374.jpg'
    response=requests.get(url,headers=headers,stream=True)
    print(response.status_code,response.reason)
    print(response.headers)
    #print(response.)
    with open('demo.jpg','wb') as fd:
        for chunk in response.iter_content(128):
            fd.write(chunk)

def download_image_improve():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
    url = 'http://ku.90sjimg.com/element_origin_min_pic/01/54/84/385747392bd3374.jpg'
    response = requests.get(url, headers=headers, stream=True)
    from contextlib import closing
    with closing(requests.get(url, headers=headers, stream=True)) as response:
        with open('demo1.jpg', 'wb') as fd:
            for chunk in response.iter_content(128):
                fd.write(chunk)



if __name__=='__main__':
    #download_image()
    download_image_improve()