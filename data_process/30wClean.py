import os,time,re
from REdealText import textParser

class loadFolders(object):
    def __init__(self,par_path):
        self.par_path=par_path
    def __iter__(self):
        for file in os.listdir(self.par_path):
            file_abspath=os.path.join(self.par_path,file)
            if os.path.isdir(file_abspath):
                yield file_abspath
class loadFiles(object):
    def __init__(self,par_path):
        self.par_path=par_path
    def __iter__(self):
        folders=loadFolders(self.par_path)
        for folder in folders:              #一级目录
            catg=folder.split(os.sep)[-1]
            for file in os.listdir(folder): #二级目录
                file_path=os.path.join(folder,file)
                if os.path.isfile(file_path):
                    this_file=open(file_path,'rb')
                    content=this_file.read().decode('utf-8')

                yield catg,content
                this_file.close()


if __name__=='__main__':
    start=time.time()
    filepath=r'./CSCMNews'
    files=loadFiles(filepath)
    n=2
    for i,msg in enumerate(files):
        if i%n==0:
            catg=msg[0]
            content=msg[1]
            content=textParser(content)
            if int(i/n)%5000==0:
                print('{t}***{i}\t docs have been dealed.'.format(i=i,t=time.strftime('%y-%m-%d %H-%M-%S',time.localtime())),'\n',catg,':\t',content[:20])






    end=time.time()
    print('Totally Cost Time:%.2f'%(end-start)+'s')