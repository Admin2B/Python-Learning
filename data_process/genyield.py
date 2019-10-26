import time

def fab1(maxnum):
    n,a,b=0,0,1
    while n<maxnum:
        #print('->',b)
        a,b=b,a+b
        n=n+1

def fab2(maxnum):
    n, a, b = 0, 0, 1
    while n<maxnum:
        yield b
        a,b=b,a+b
        n=n+1

def GeneratorDome():
    start_time=time.time()
    maxnum=500
    fab1(maxnum)
    end_time=time.time()
    print(end_time-start_time,'s')

    start1_time = time.time()
    b=fab2(maxnum)
    end1_time = time.time()
    print(end1_time - start1_time, 's')
    print(b)

if __name__=='__main__':
    #fab1(1000)
    GeneratorDome()

    #  https://blog.csdn.net/mieleizhi0522/article/details/82142856
    # def foo():
    #     print("starting...")
    #     while True:
    #         res = yield 4
    #         print("res:", res)
    #
    #
    # g = foo()
    # print(next(g))
    # print("*" * 20)
    # print(next(g))
    # print(next(g))
    # print(next(g))
