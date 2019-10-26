#encoding=utf-8
import numpy as np
from numpy.linalg import inv
from numpy import dot
from numpy import mat

# #y=2x
# X=mat([1,2,3]).reshape(3,1)
# Y=2*X
#
# #theta=(X'X)^-1X'Y
# #theta=dot(dot(inv(dot(X.T,X)),X.T),Y)
#
# #theta=theta-alpha*(theta*X-Y)*X
# theta=1.0
# alpha=0.1
# for i in range(100):
#     theta=theta+np.sum(alpha*(Y-dot(theta,X))*X.reshape(1,3))/3.0
#
#
# print(theta)

import pandas as pd
dataset=pd.read_csv('data.csv')
#print(dataset)
temp=dataset.iloc[:,2:5]
temp['x0']=1
X=temp.iloc[:,[3,0,1,2]]
#print(X)
Y=dataset.iloc[:,1].values.reshape(150,1)
#print(Y)
theta=dot(dot(inv(dot(X.T,X)),X.T),Y)
print(theta)

theta=np.array([1.,1.,1.,1.]).reshape(4,1)
alpha=0.01
temp=theta
X0=X.iloc[:,0].values.reshape(150,1)
X1=X.iloc[:,1].values.reshape(150,1)
X2=X.iloc[:,2].values.reshape(150,1)
X3=X.iloc[:,3].values.reshape(150,1)

for i in range(10000):
    theta[0]=theta[0]+alpha*np.sum((Y-dot(X,theta))*X0)/150.
    theta[1] = theta[1] + alpha * np.sum((Y - dot(X, theta)) * X1) / 150.
    theta[2] = theta[2] + alpha * np.sum((Y - dot(X, theta)) * X2) / 150.
    theta[3] = theta[3] + alpha * np.sum((Y - dot(X, theta)) * X3) / 150.
    theta=temp
print(theta)



