import os,time

class TraversalFun():
    def __init__(self,rootDir):
        self.rootDir=rootDir
    def TraversalDir(self):
        TraversalFun.AllFiles(self,self.rootDir)

    def AllFiles(self,rootDir):
        for lists in os.listdir(rootDir):
            path=os.path.join(rootDir,lists)
            if os.path.isfile(path):
                print(os.path.abspath(path))
            elif os.path.isdir(path):
                TraversalFun.AllFiles(self,path)
if __name__=='__main__':
    time_start=time.time()
    rootDir=r'../paper'
    tra=TraversalFun(rootDir)
    tra.TraversalDir()
    time_end=time.time()
    print('Totally cost:',time_end-time_start,'s')