c=3000
d=100.0
e="aaaaaa"
print(c)
print(d)
print(e)

a=b=c=1
print(a,b,c)

a,b,c=1,2,"ddd"
print(a,b,c)

#数据类型
#a,b,c.d=1,2.0,"bbb",True
#print(type(a),type(b),type(c),type(d))

a=111
#isinstance用于判断类型
print(isinstance(a,int))

print("------------------------")

#数值运算
print(5+1)
print(5-1)
print(5*2)
print(5%3)
print(5/2)
print(5//2) #得到一个整数
print(5**2) #乘方

#列表
list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
tinylist = [123, 'runoob']

print("输出完整列表:",list)
print("输出列表中第一个元素",list[0])
print("输出列表中的第一个元素到第三个元素",list[1:3])
print("输出列表从第二个元素到所有元素",list[2:])
print("拼接列表",list+tinylist)

print("------------------------------------------")

#元组
list1 = ( 'abcd', 786 , 2.23, 'runoob', 70.2)
tinylist1 = (123, 'runoob')
print("输出完整元组:",list1)
print("输出元组中第一个元素",list1[0])
print("输出元组中的第一个元素到第三个元素",list1[1:3])
print("输出元组从第二个元素到所有元素",list1[2:])
print("拼接元组",list1+tinylist1)

print("-------------------------------------")

#集合
student={"aaa","bbb","ccc"}
print("输出集合",student)
#判断集合
if "bbb" in student:
    print("在集合")
else:
    print("不在集合")
#差集
student1={"bbb","ddd"}
print("两个集合的差集",student-student1)
#并集
print("两个集合的并集",student1|student)
print("两个集合的交集",student1&student)
print("两个集合不同存在的元素",student1^student)

print("-------------------------")
#字典
dic={"name":"黄国栋","age":22,"学历":"大专"}
print("输出所有字典",dic)
print("输出字典中的键",dic.keys())
print("输出字典中的值",dic.values())

