import os,fnmatch
from win32com import client as wc
from win32com.client import Dispatch

def Word2Txt(filePath,savePath=''):
    #获取文件路径及格式
    dirs,filename=os.path.split(filePath)
    #print(dirs,'\n',filename)
    new_name=''
    if fnmatch.fnmatch(filename,'*.doc') or fnmatch.fnmatch(filename,'*.DOC'):
        new_name=filename[:-4]+'.txt'
    elif fnmatch.fnmatch(filename,'*.docx') or fnmatch.fnmatch(filename,'*.DOCX'):
        new_name=filename[:-5]+'.txt'
    else:
        print('格式不正确，仅支持doc或docx格式。')
        return
    #设置新文件保存路径
    if savePath=='' :
        savePath=dirs
    else:
        savePath=savePath
    word2txtPath=os.path.join(savePath,new_name)
    print('-->',word2txtPath)
    #加载文本处理
    wordapp=wc.Dispatch('Word.Application')
    mytxt=wordapp.Documents.Open(filePath)
    #保存文本
    mytxt.SaveAs(word2txtPath,4)    #参数4代表抽取文本
    mytxt.Close()





if __name__=='__main__':
    filePath=os.path.abspath(r'../1.doc')
    Word2Txt(filePath)