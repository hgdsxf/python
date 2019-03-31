#Author:黄国栋

verser=[1,2,3,4,5]

#查询
print("输出序列第三个元素",verser[2])
print("输出最后一个元素",verser[-1])

#切片查询
print("输出第二个到第五个元素",verser[1:4])
print("输出第一个、第二个、第三个元素",verser[0:1:2])

#两个序列相加
verser1=[6,7,8,9,10]
print("两个序列相加",verser+verser1)

#序列相乘
print("序列相乘",verser*2)

#判断某个元素是否是序列的成员
print("判断1是否是verser的成员",1 in verser)

#计算序列的长度
print("获取verser序列的长度",len(verser))

#最大值
print("获取verser的最大值",max(verser))

#最小值
print("获取verser的最小值",min(verser))