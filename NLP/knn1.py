#encoding: utf-8
import numpy as np
from numpy import *
import matplotlib
import matplotlib.pyplot as plt
import math
import operator


def creat_datasets():
    datasets=array([[8,4,2],[7,1,1],[1,4,4],[3,0,5]])
    labels=['非常热','非常热','一般热','一般热']
    return datasets,labels

def analyze_data_plot(x,y):
    fig=plt.figure()
    ax=fig.add_subplot(111)
    ax.scatter(x,y)

    plt.title('游客冷热感知散点图',fontsize=15)
    plt.xlabel('天热吃冰淇淋数目',fontsize=15)
    plt.ylabel('天然喝水数目',fontsize=15)
    plt.savefig('datashow',bbox_inches='tight')
    plt.show()


def knn_Classifier(newV,datasets,labels,k):
    SqrtDist=ComputeEuclideanDistance3(newV,datasets)
    sortDistindexs=SqrtDist.argsort(axis=0)
    classCount={}
    for i in range(k):
        votelabel=labels[sortDistindexs[i]]
        #print(sortDistindexs[i],votelabel)
        classCount[votelabel]=classCount.get(votelabel,0)+1
    #print(classCount)
    sortedClassCount=sorted(classCount.items(),key=operator.itemgetter(0),reverse=True)
    #print(newV,'KNN投票预测结果：',sortedClassCount[0][0])
    return sortedClassCount[0][0]



def ComputeEuclideanDistance1(x1,y1,x2,y2):
    d=math.sqrt(math.pow((x1-x2),2)+math.pow((y1-y2),2))
    return d

def ComputeEuclideanDistance2(instance1,instance2,length):
    d=0
    for x in range(length):
        d=d+pow(instance1[x]-instance2[x],2)
    return sqrt(d)

def ComputeEuclideanDistance3(newV,datasets):
    rowsize,colsize=datasets.shape
    diffMat=tile(newV,(rowsize,1))-datasets
    sqrtDiffMat=diffMat**2
    #print(diffMat)
    SqrtDist=sqrtDiffMat.sum(axis=1)**0.5
    #print(SqrtDist)
    return SqrtDist




if __name__=='__main__':
    datasets,labels=creat_datasets()
    #print('数据集：\n',datasets,'\n','类标签\n',labels)

    #analyze_data_plot(datasets[:,0],datasets[:,1])

    # d=ComputeEuclideanDistance(2,4,8,2)
    #d=ComputeEuclideanDistance([2,4],[8,2],2)
    #ComputeEuclideanDistance3([2,4,4],datasets)
    #print(d)


    # newW=[2,4,4]
    # res=knn_Classifier(newW,datasets,labels,3)


    vecs=array([[2,4,4],[3,0,0],[5,7,2]])
    for vec in vecs:
        res = knn_Classifier(vec, datasets, labels, 3)
        print(vec, 'KNN投票预测结果：', res)


