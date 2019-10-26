import re


def filter_tags(htmlstr):
    htmlstr=' '.join(htmlstr.split())
    re_doctype=re.compile(r'<!DOCTYPE .*?>',re.S)
    res=re_doctype.sub('',htmlstr)
    return res


def readFile(path):
    str_doc=''
    with open(path,'r',encoding='utf-8') as f:
        str_doc=f.read()
    return str_doc

if __name__=='__main__':
    str_doc=readFile(r'html.txt')
    res=filter_tags(str_doc)
    print(res)