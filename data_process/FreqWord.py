from nltk import *

def readFile(path):
    str_doc=''
    with open(path,'r',encoding='utf-8') as f:
        str_doc=f.read()
    return str_doc


if __name__=='__main__':
