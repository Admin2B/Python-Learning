import os,fnmatch
from win32com import client as wc
from win32com.client import Dispatch

def File2Txt(filePath,savePath=''):
    # 获取文件路径及格式
    dirs, filename = os.path.split(filePath)
    # print(dirs,'\n',filename)
    new_name = ''
    typename=os.path.splitext(filename)[-1].lower()
    new_name=TranType(filename,typename)

    # 设置新文件保存路径
    if savePath == '':
        savePath = dirs
    else:
        savePath = savePath
    new2txtPath = os.path.join(savePath, new_name)
    print('-->', new2txtPath)

    # 加载文本处理
    docapp = wc.Dispatch('Word.Application')
    mytxt = docapp.Documents.Open(filePath)

    # 保存文本
    mytxt.SaveAs(new2txtPath, 4)  # 参数4代表抽取文本
    mytxt.Close()


def TranType(filename,typename):
    new_name=''
    if typename=='.pdf':
        if fnmatch.fnmatch(filename,'*.pdf'):
            new_name=filename[:-4]+'.txt'
        else:
            return
    elif typename=='.doc' or typename=='.docx':
        if fnmatch.fnmatch(filename,'*.doc'):
            new_name=filename[:-4]+'.txt'
        elif fnmatch.fnmatch(filename,'*.docx'):
            new_name=filename[:-5]+'.txt'
        else:
            return
    else:
        print('警告：\n您输入的',typename,'格式不合法。')
        return
    return new_name



if __name__=='__main__':
    filePath = os.path.abspath(r'../1.doc')
    File2Txt(filePath)