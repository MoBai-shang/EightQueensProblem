import turtle
import math
import time
import random
import numpy as np
import matplotlib.pyplot as plt
def plotstatus(status):#画出问题的解
    for i in range(len(status)):
        plt.plot(i+0.5,status[i]+0.5,'r*')
    plt.grid()
    plt.xlim(-0.2,8.2)
    plt.ylim(-0.2,8.2)
    newx=np.linspace(0,8,9)
    newy=np.linspace(0,8,9)
    plt.xticks(newx)
    plt.yticks(newy)

def conflict_value(status):#计算各状态下冲突皇后对数
    s=0
    for i in range(len(status)):
        for j in range(i+1,len(status)):
            if status[i]==status[j]:
                s+=1
            if math.fabs(status[i]-status[j])==j-i:
                s+=1
    return s
def climb(status,value):#爬山法算法，status为状态，value为该状态所对应的皇后冲突对数
    change=[]
    result=[]
    for i in range(len(status)):
        for j in range(len(status)):
            if status[i]==j:
                continue
            statu=list(status)
            statu[i]=j#将第i列皇后的位置放在第j行
            value1=conflict_value(statu)
            if value1<=value:#当改变后的状态所对应的冲突皇后数不增加时，表明该状态为下次迭代的候选状态之一
                 value=value1
                 change.append([i,j,value1])
    for i in range(len(change)):#从候选状态中选择出冲突皇后对数最少的那些状态
        if change[i][2] == value:
            result.append(change[i])
    if len(result):#随机选择一个最好状态使用
        t=random.randint(0,len(result)-1)
        x2 = result[t][1]
        x1 = result[t][0]
        status[x1]=x2
    return status
if __name__ == '__main__':
    start=time.clock()
    fx=[]
    for f in range(1000):#进行一千次测试
        total=0
        status = []
        for im in range(8):#随机产生初始状态
            t = random.randint(0, 7)
            status.append(t)
        while total<20:#对爬山法每次使用向上爬升的次数限制

            value=conflict_value(status)
            #print(status)
            if value == 0:
                if status not in fx:#将解放入解集
                    fx.append(status)
                    print(status)
                break
            status=climb(status,value)
            total+=1
    end=time.clock()
    print(len(fx),end-start)
    if len(fx)!=0:
        print((end-start)/len(fx))#计算出平均每个解的求算时间

    for w in range(len(fx)):#为每个解可视化
        plt.subplot(5,5,w%25+1)
        plotstatus(fx[w])
        if w%25+1==25:
            plt.show()
        print(fx[w],end=' ')#打印出每个解
        if w%5==4:
            print('\n')
    plt.show()
    '''
    92, 13.60629596989143s
    '''