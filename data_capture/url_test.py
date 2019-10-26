from urllib import request
from urllib.request import Request
from  urllib import parse

url_demo='https://www.google.com/search?'
req=request.Request(url_demo)

postData=parse.urlencode([
    ('source','hp'),
    ('ei','9l89XaLCM46WtQWBh43gDQ'),
    ('q','qq'),
    ('oq','qq'),
    ('gs_l','psy-ab.3...0.0..156...0.0..0.0.0.......0......gws-wiz.GNwsYD_CYw0'),
    ('ved','0ahUKEwiilbGMnNfjAhUOS60KHYFDA9wQ4dUDCAU'),
    ('uact','5')
])

req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36')
resp=request.urlopen(req,data=postData.encode('utf-8'))

print(resp.read().decode('utf-8'))

