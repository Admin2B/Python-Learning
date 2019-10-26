#encoding=utf-8
import numpy as np
import  pandas as pd
import matplotlib.pylab as plt
class Perceptron (object):
    '''
    eta:学习率
    n_iter:迭代次数
    w_:权重向量
    errors:误差
    '''
    def __init__(self,eta=0.01,n_iter=10):
        self.eta=eta
        self.n_iter=n_iter

    def predict(self, X):
        return np.where(self.net_input(X) >= 0.0, 1, -1)

    def net_input(self, X):
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def fit(self,X,y):
        '''
        :param X:输入数据
        :param y:样本分类
        :return:
        X:shape[n_samples,n_features]
        X:[[1,2,3],[4,5,6]]  n_samples:2  n_features:3
        y:[1,-1]
        '''
        '''
        初始化权重向量为0
        '''
        self.w_=np.zeros(1+X.shape[1])
        self.errors_=[]
        for _ in range(self.n_iter):
            errors=0

            for xi,target in zip (X,y):
                update=self.eta*(target-self.predict(xi))
                self.w_[1:]+=update*xi
                self.w_[0] += update

                errors+=int(update!=0.0)
                self.errors_.append(errors)






def main():
    file='data.csv'
    df=pd.read_csv(file,header=None)
    print(df.head(10))
    y=df.loc[0:99,4].values
    print(y)
    y=np.where(y=='Iris-versicolor',-1,1)
    print(y)
    X=df.loc[0:99,[0,2]].values
    print(X)
    #plt.scatter(X[:49,0],X[:49,1],color='red',marker='o',label='setosa')
    #plt.scatter(X[50:99, 0], X[50:99, 1], color='blue', marker='x', label='versicolor')
    plt.xlabel('花瓣长度')
    plt.ylabel('花径长度')
    plt.legend(loc='upper left')
    #plt.show()

    ppn=Perceptron(eta=0.01,n_iter=10)
    ppn.fit(X,y)
    plt.plot(range(1,len(ppn.errors_)+1),ppn.errors_,marker='o')
    plt.xlabel=('Epochs')
    plt.ylabel=('错误分类次数')
    plt.show()

    from matplotlib.colors import ListedColormap
    def plot_decision_regions(X,y,classifier ,resolution=0.02):
        maker=('s','x','o','v')
        colors=('red','blue','lightgreen','gray','cyan')
        cmap=ListedColormap(colors[:len(np.unique(y))])
        x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max()
        x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max()
        #print(x1_min,x1_max)
        #print(x2_min,x2_max)
        xx1,xx2=np.meshgrid(np.arange(x1_min,x1_max,resolution),
                            np.arange(x2_min,x2_max,resolution))
        #print(np.arange(x1_min,x1_max,resolution).shape)
        #print(np.arange(x1_min,x1_max,resolution))
        #print(xx1.shape)
        #print(xx1)

        Z=classifier.predict(np.array([xx1.ravel(),xx2.ravel()]).T)
        print(xx1.ravel())
        print(xx2.ravel())
        print(Z)
        Z=Z.reshape(xx1.shape)
        plt.contourf(xx1,xx2,Z,alpha=0.4,cmap=cmap)
        plt.xlim(xx1.min(),xx1.max())
        plt.ylim(xx2.min(),xx2.max())

        for idx,cl in enumerate(np.unique(y)):
            plt.scatter(x=X[y==cl,0],y=X[y==cl,1],alpha=0.8,c=cmap(idx),
            marker=maker[idx],label=cl)




    plot_decision_regions(X,y,ppn,resolution=0.02)
    #plt.xlabel('花径长度')
    #plt.ylabel('花瓣长度')
    plt.legend(loc='upper left')
    plt.show()


if __name__=='__main__':
    main()