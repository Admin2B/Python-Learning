
import re

def textParser(str_doc):
    #正则过滤特殊符号，标点，英文，数字
    r1='[a-zA-Z0-9，。？/‘’“”：；、！]+'
    r2='\s+'
    str_doc=re.sub(r1,' ',str_doc)
    str_doc=re.sub(r2,' ',str_doc)
    str_doc=str_doc.replace('\n','')
    return str_doc


def readFile(path):
    str_doc=''
    with open(path,'r',encoding='utf-8') as f:
        str_doc=f.read()
    return str_doc


if __name__=='__main__':
    path=r'./CSCMNews/体育/0.txt'
    str_doc=readFile(path)
    print(str_doc)
    mystr=textParser(str_doc)
    print(mystr)