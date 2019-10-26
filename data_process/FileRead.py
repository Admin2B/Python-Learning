import os,time

def TraversalDir(rootDir):

    for i,lists in enumerate(os.listdir(rootDir)):
        path=os.path.join(rootDir,lists)

        if os.path.isfile(path):
            if i%10000==0:
                print('{t}***{i}\t docs has been read'.format(i=i,t=time.strftime('%y-%m-%d %H:%M:%S',time.localtime())))


        if os.path.isdir(path):
            TraversalDir(path)

if __name__=='__main__':
    rootDir=r'./CSCMNews'
    t1=time.time()
    TraversalDir(rootDir)
    t2=time.time()
    print('Totally cost time:%.2f'%(t2-t1)+'s')