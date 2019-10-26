import sys
from numpy import *

def loadData(fn):
    dataMat=[]
    labelMat=[]
    fi=open('./'+fn)
    for line in fi:
        fd=line.strip().split('\t')
        dataMat.append([1.0,float(fd[0]),float(fd[1])])
        labelMat.append(int(fd[2]))
    return dataMat,labelMat

def getW(x,y):
    dataMatrix=mat(x)     #400*3
    labelMatrix=mat(y).transpose()   #400*1
    m,n=shape(dataMatrix)       #400,3
    weights=ones((n,1))         #3*1
    alpha=0.01
    max_loop=500
    for i in range(max_loop):
        y_pre=sigmoid(dataMatrix*weights)   #400*1
        error=labelMatrix-y_pre             #400*1
        grad=dataMatrix.transpose()*error   #3*1
        weights=weights+alpha*grad          #3*1
    return weights

def sigmoid(z):
    return 1.0/(1+exp(-z))

if __name__=='__main__':
    ###
    #-4*1+2*x1-x2=[1,x1,x2]*[-4,2,-1].T
    #x(400,3) y(400,1)  w(3,1)

    ####
    x,y=loadData('train.txt')
    w=getW(x,y)
    #print (w)
    tx,ty=loadData('test.txt')
    y_pre=sigmoid(mat(tx)*w)    #400*1 =====[0,1]
    y_pre_label=(sign(y_pre-0.5)+1)/2
    tp,tn,fp,fn=0,0,0,0
    for k in range(len(ty)):
        if y_pre_label[k]==1 and ty[k]==1:
            tp+=1
        if y_pre_label[k]==0 and ty[k]==0:
            tn+=1
        if y_pre_label[k] == 1 and ty[k] == 0:
            fp += 1
        if y_pre_label[k]==0 and ty[k]==1:
            fn+=1
    print('tp:',tp)
    print('tn:', tn)
    print('fp:', fp)
    print('fn:', fn)