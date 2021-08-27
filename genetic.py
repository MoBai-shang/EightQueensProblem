import turtle
import math
import random
import numpy as np
import matplotlib.pyplot as plt
import time
def value(status):#计算出对应于状态status下不相互冲突的皇后对数
    s = 0
    for i in range(len(status)):
        for j in range(i + 1, len(status)):
            if status[i] == status[j]:
                s += 1
            if math.fabs(status[i] - status[j]) == j - i:
                s += 1
    return 28-s
def gen():#定义遗传函数，该函数随机产生状态祖先并就其遗传迭代
    status = []
    example_num = 10#祖先状态数
    queen_num = 8#每一个状态的长度
    max_value = int(queen_num * (queen_num - 1) / 2)#不冲突皇后数的最大值
    # 随机产生状态数组status
    for i in range(example_num):
        statu = []
        for j in range(queen_num):
            statu.append(random.randint(0, queen_num - 1))
        status.append(list(statu))
    generation=0
    while generation<totalgeneration:#当遗传代数超过某数时，不再遗传迭代
        #print(status)
        n=len(status)
        lim=[]
        for i in range(n):#计算状态数组status中各状态所对应的不冲突对数
            f=value(status[i])
            if f==max_value:#成功条件
                print('状态', status[i],'不互相攻击对数为',f)
                if status[i] not in fx:#将成功的状态不重复地放于fx中
                    fx.append(list(status[i]))
            lim.extend([i]*f)#计算状态status[i]所对应的杂交频率，即lim数组中值为i的元素占总元素的比
        s=len(lim)
        copy=[]

        for im in range(nextnum):#in range(total),每次由状态数组status产生的子代总数为total
            num1=random.randint(0,s-1)#参与杂交的第一个状态编号
            num2=random.randint(0,s-1)#参与杂交的第二个状态编号
            num3=random.randint(1,len(status[0])-1)#杂交点位
            wx1=lim[num1]
            wx2=lim[num2]
            example1=list(status[wx1])#参与杂交的第一个状态
            example2=list(status[wx2])#参与杂交的第二个状态
            #杂交
            #print('example',example1,example2,value(example1),value(example2))
            example1[num3:],example2[num3:]=example2[num3:],example1[num3:]
            if value(example1)==max_value:#成功条件
                print('状态',example1,'不互相攻击对数为',value(example1))
                if example1 not in fx:#将成功的状态不重复地放于fx中
                    fx.append(list(example1))
            if value(example2) == max_value:  # 成功条件
                print('状态',example2,'不互相攻击对数为', value(example2))
                if example2 not in fx:  # 将成功的状态不重复地放于fx中
                    fx.append(list(example2))
            #print('杂交',example1,example2,value(example1),value(example2))
            #产生变异点
            point1=random.randint(0,len(example1)-1)
            point2=random.randint(0,len(example2)-1)
            #变异点位变异后的值
            point1_num=random.randint(0,len(example1)-1)
            point2_num=random.randint(0,len(example2)-1)
            #变异
            example1[point1]=point1_num
            example2[point2]=point2_num
            #print('变异', example1, example2,value(example1),value(example2))
            copy.extend([example1,example1])
        status=copy
        generation+=1

if __name__ == '__main__':
    global fx
    global queen_num
    global max_value
    global totalgeneration
    global nextnum
    global limit
    start = time.clock()
    fx=[]
    f=0
    status=[]
    queen_num = eval(input('请输入皇后的个数:\n'))  # 每一个状态的长度
    example_num = 10  # 祖先状态数
    totalgeneration = eval(input('请输入遗传迭代的总代数，如：150\n'))  # 遗传迭代总次数
    limit = eval(input('请输入遗传算法的使用总次数，如：20\n'))  # 遗传算法的使用次数
    nextnum = eval(input('请输入每次遗传迭代生成子代的个数，如：700\n'))  # 每次遗传迭代生成子孙的个数
    max_value = int(queen_num * (queen_num - 1) / 2)
    while f < limit:#num<s,s为进行遗传算法的次数
        gen()
        f+=1
        print('第%d次遗传循环结束'%f,'目前共找到解',len(fx),'个')
    end = time.clock()
    if len(fx)==0:
        bi=0
    else:
        bi=(end-start)/len(fx)
    print('循环%d次,' % limit, '更迭子代数%d个,' % nextnum, '遗传%d代,' % totalgeneration, '找到解', len(fx),'个,耗时%.2fs' % (end - start),'平均每解时%.2f'%bi)
    print('下面是找到的解')
    print(fx)
    over=input()
'''
循环50次, 更迭子代数200个, 遗传100代, 找到解 24 个,耗时84.26s
循环20次, 更迭子代数500个, 遗传150代, 找到解 33 个,耗时132.97s
循环20次, 更迭子代数500个, 遗传200代, 找到解 32 个,耗时170.04s
循环20次, 更迭子代数800个, 遗传150代, 找到解 43 个,耗时229.22s 
循环20次, 更迭子代数100个, 遗传50代, 找到解 3 个,耗时8.32s 平均每解时2.77
循环20次, 更迭子代数100个, 遗传100代, 找到解 4 个,耗时17.20s 平均每解时4.30
循环20次, 更迭子代数100个, 遗传150代, 找到解 9 个,耗时26.57s 平均每解时2.95 
循环20次, 更迭子代数100个, 遗传200代, 找到解 7 个,耗时38.33s 平均每解时5.48
循环20次, 更迭子代数20个, 遗传150代, 找到解 4 个,耗时7.24s 平均每解时1.81
循环20次, 更迭子代数50个, 遗传150代, 找到解 6 个,耗时17.11s 平均每解时2.85
循环20次, 更迭子代数100个, 遗传150代, 找到解 5 个,耗时29.96s 平均每解时5.99
循环20次, 更迭子代数150个, 遗传150代, 找到解 12 个,耗时42.44s 平均每解时3.54
循环20次, 更迭子代数200个, 遗传150代, 找到解 13 个,耗时57.92s 平均每解时4.46
循环20次, 更迭子代数250个, 遗传150代, 找到解 24 个,耗时68.81s 平均每解时2.87
循环20次, 更迭子代数300个, 遗传150代, 找到解 27 个,耗时83.02s 平均每解时3.07
循环20次, 更迭子代数400个, 遗传150代, 找到解 27 个,耗时107.64s 平均每解时3.99
循环200次, 更迭子代数250个, 遗传150代, 找到解 86 个,耗时683.86s 平均每解时7.95
循环5次, 更迭子代数250个, 遗传1000代, 找到解 31 个,耗时110.25s 平均每解时3.56
循环5次, 更迭子代数450个, 遗传1000代, 找到解 42 个,耗时201.89s 平均每解时4.81
'''
