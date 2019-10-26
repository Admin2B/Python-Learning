#coding=utf-8

import numpy as np
import pandas as pd
import matplotlib.pylab as plt

class AdalineGD(object):

    '''
    eta:学习率0-1
    n_iter:迭代次数
    w_:存储权重向量
    error_:网络对数据进行错误判断的次数
    '''
    def __init__(self,eta=0.01,n_iter=50):
        self.eta=eta
        self.n_iter=n_iter
    def fit(self,X,y):
        '''
        X:二维数组，[n_samples(训练条目数),n_features(特征数)]
        y:一维向量，存储每一训练条目正确分类
        '''
        self.w_=np.zeros(1+X.shape[1])
        self.cost_=[]

        for i in range(self.n_iter):
            output=self.net_input(X)
            errors=(y-output)
            self.w_[1:]+=self.eta*X.T.dot(errors)
            cost=(errors**2).sum()/2.0
            self.cost_.append(cost)
            return self

    def net_input(self, X):
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def activation(self,X):
        return self.net_input(X)

    def predict(self,X):
        return np.where(self.activation(X)>=0,1,0)








def main():
    file = 'data.csv'
    df = pd.read_csv(file, header=None)
    y = df.loc[0:99, 4].values
    y = np.where(y == 'Iris-versicolor', -1, 1)
    X = df.loc[0:99, [0, 2]].values
    # print(X)
    # print(y)

    ada=AdalineGD(eta=0.0001,n_iter=50)
    ada.fit(X,y)

    from matplotlib.colors import ListedColormap
    def plot_decision_regions(X, y, classifier, resolution=0.02):
        maker = ('s', 'x', 'o', 'v')
        colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
        cmap = ListedColormap(colors[:len(np.unique(y))])
        x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max()
        x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max()
        # print(x1_min,x1_max)
        # print(x2_min,x2_max)
        xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                               np.arange(x2_min, x2_max, resolution))
        # print(np.arange(x1_min,x1_max,resolution).shape)
        # print(np.arange(x1_min,x1_max,resolution))
        # print(xx1.shape)
        # print(xx1)

        Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
        print(xx1.ravel())
        print(xx2.ravel())
        print(Z)
        Z = Z.reshape(xx1.shape)
        plt.contourf(xx1, xx2, Z, alpha=0.4, cmap=cmap)
        plt.xlim(xx1.min(), xx1.max())
        plt.ylim(xx2.min(), xx2.max())

        for idx, cl in enumerate(np.unique(y)):
            plt.scatter(x=X[y == cl, 0], y=X[y == cl, 1], alpha=0.8, c=cmap(idx),
                        marker=maker[idx], label=cl)

    plot_decision_regions(X,y,classifier=ada,resolution=0.02)
    plt.title('Adaline-Gradient descent')
    plt.xlabel('Flower Diameter Length')
    plt.ylabel('Petal Length')
    plt.legend(loc='upper left')
    plt.show()

    plt.plot(range(1,len(ada.cost_)+1),ada.cost_,marker='o')
    plt.xlabel('Epoches')
    plt.ylabel('Sum-Squared-Error')
    plt.show()







if  __name__=='__main__':
    main()