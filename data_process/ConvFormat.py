import os,time
import ExtractText.ExtractTxt as ET

class TraversalFun():
    def __init__(self,rootDir,func=None,saveDir=''):
        self.rootDir=rootDir
        self.func=func
        self.saveDir=saveDir


    def TraversalDir(self):
        dirs,filename=os.path.split(self.rootDir)
        save_dir=''
        if self.saveDir=='':
            save_dir=os.path.abspath(os.path.join(dirs,'new_'+filename))
        else:
            save_dir=self.saveDir

        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        print('保存目录:\n',save_dir)

        TraversalFun.AllFiles(self,self.rootDir,save_dir)

    def AllFiles(self,rootDir,save_dir=''):
        for lists in os.listdir(rootDir):
            path=os.path.join(rootDir,lists)
            if os.path.isfile(path):
                self.func(os.path.abspath(path),os.path.abspath(save_dir))
            if os.path.isdir(path):
                newpath=os.path.join(save_dir,lists)
                if not os.path.exists(newpath):
                    os.makedirs(newpath)
                TraversalFun.AllFiles(self,path,newpath)

if __name__=='__main__':
    time_start=time.time()

    rootDir=r'./paper'
    tra=TraversalFun(rootDir,ET.File2Txt)
    tra.TraversalDir()

    time_end=time.time()
    print('Totally cost:',time_end-time_start,'s')