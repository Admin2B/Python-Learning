from sklearn import neighbors
from numpy import *


def creat_dataset2():
    datasets = array([[8,4,2],[7,1,1],[1,4,4],[3,0,5],[9,4,2],[7,0,1],[1,5,4],[4,0,5]])#数据集
    labels = ['非常热','非常热','一般热','一般热','非常热','非常热','一般热','一般热']#类标签
    return datasets,labels

def knn_sklearn_predict():
    knn=neighbors.KNeighborsClassifier()
    datasets,labels=creat_dataset2()
    knn.fit(datasets,labels)

    predictRes=knn.predict([[2,4,0]])
    print(predictRes)
    return predictRes

if __name__=='__main__':
    predictRes=knn_sklearn_predict()


