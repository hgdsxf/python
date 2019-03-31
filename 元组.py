#Author:黄国栋
tuplename=(1,2,3,4,5)

#元组的类型
print("元组的类型",type(tuplename))

#创建数值元组
yuanzu=tuple(range(10,20,2))
print("tuple",yuanzu)

verser=("春眠不觉晓","python不得了","夜来爬数据","好评值多少")
#del verser
#print("删除元组",verser)

#访问
print("访问元组中第二个元素",verser[1])
print("访问元组的第一个到最后的一个元素",verser[0:])

#遍历
for i in verser:
    print(i)

print("")
#修改元组
#verser[3]="拿铁"
print("修改后的元组",verser)