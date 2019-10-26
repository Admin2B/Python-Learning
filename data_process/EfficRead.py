import os,time

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
                yield catg,file

if __name__=='__main__':
    start_time=time.time()
    filepath=os.path.abspath(r'./CSCMNews')
    files=loadFiles(filepath)
    for i,msg in enumerate(files):
        if i%10000==0:
            print('{t}***{i}\t docs have been read.'.format(i=i,t=time.strftime('%y-%m-%d %H:%M:%S',time.localtime())))
    end_time=time.time()
    print('Totally cost time:%.3f'%(end_time-start_time)+'s')








