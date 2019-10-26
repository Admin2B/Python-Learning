# encoding=utf-8

import numpy as np
from numpy.linalg import *
def Main():
    lst=[[1,3,5],[2,4,6]]
    print(type(lst))
    np_list=np.array(lst)
    print(type(np_list))
    np_lst=np.array(lst,dtype=np.float)
    #bool,
    print(np_lst.shape)
    print(np_lst.ndim)
    print(np_lst.dtype)
    print(np_lst.itemsize)
    print(np_lst.size)
    print(np.random.rand(2,5))



    print(np.eye(3))
    mat=np.array([[1,2],[3,4]])
    print(inv(mat))

if __name__=="__main__":
    Main()