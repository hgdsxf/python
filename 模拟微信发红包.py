#红包生成思路
#200 块钱 10个红包
#0-200 的一个轴,随机取9个点,分成10段, 每一段的值表示一个红包的大小
#把输入的 money值 * 100 拿到的数值就是分, 不用再考虑单位是元的时候 保留2位小数
import random

m=int(input("请输入您要发的红包:"))
n=int(input("请输入您要发的包数:"))


def red_pocket(money,num):
    money = money * 100     #把元 换算成分
    ret = random.sample(range(1,money),num-1)
    ret.sort()
    ret.insert(0,0)
    ret.append(money)
    for i in range(len(ret)-1):
        gap = (ret[i+1] - ret[i])/100  #算出每一段的差值,再除以100 转换成单位元
        yield gap  # 分回一个生成器, 在抽红包之前就已经分好了,然后按照抽的顺序弹出红包金额

red_g = red_pocket(m,n)
item=-1
for i in red_g:
    item+=1;
    print("第"+str(item+1)+"个红包:"+str(i)+"元")