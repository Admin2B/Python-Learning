import re
import jieba
import sys

#读取文本
def readFile(path):
    str_doc=''
    with open(path,'r',encoding='utf-8') as f:
        str_doc=f.read()
    return str_doc

#正则清洗数据
def textParser(str_doc):
    #去掉字符
    str_doc=re.sub('\u3000','',str_doc)
    #去掉空格
    str_doc=re.sub('\s+','',str_doc)
    #去掉换行符
    str_doc=str_doc.replace('\n',' ')
    str_doc=re.sub('[a-zA-Z0-9，。？/‘’“”：；、！]+','',str_doc)
    return str_doc


def get_stop_words():
    


#利用jieba分词对文本进行分词，返回切词后的list
def seg_doc(str_doc):
    sent_list=str_doc.split('\n')
    sent_list=map(textParser,sent_list)
    print(sent_list)

if __name__=='__main__':
    path=r'./CSCMNews/体育/0.txt'
    str_doc=readFile(path)
    print(str_doc)
    #print(textParser(str_doc))
    seg_doc(str_doc)
