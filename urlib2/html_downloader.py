import urllib
class HtmlDownloader(object):


    def download(self,url):
        if url is None:
            return None
        response=urllib.requset.urlopen(url)

        if response.getcode()==200:
            return response.read()
        else:
            return None

