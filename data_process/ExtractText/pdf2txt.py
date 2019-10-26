import os,fnmatch
from win32com import client as wc
from win32com.client import Dispatch

def Pdf2Txt(filePath,savePath=''):
    #获取文件路径及格式
    dirs,filename=os.path.split(filePath)
    #print(dirs,'\n',filename)
    new_name=''
    if fnmatch.fnmatch(filename,'*.pdf') or fnmatch.fnmatch(filename,'*.PDF'):
        new_name=filename[:-4]+'.txt'
    else:
        print('格式不正确，仅支持pdf格式。')
        return
    #设置新文件保存路径
    if savePath=='' :
        savePath=dirs
    else:
        savePath=savePath
    pdf2txtPath=os.path.join(savePath,new_name)
    print('-->',pdf2txtPath)
    #加载文本处理
    pdfapp=wc.Dispatch('Word.Application')
    mytxt=pdfapp.Documents.Open(filePath)
    #保存文本
    mytxt.SaveAs(pdf2txtPath,4)    #参数4代表抽取文本
    mytxt.Close()


if __name__=='__main__':
    filePath=os.path.abspath(r'./2.pdf')
    Pdf2Txt(filePath)