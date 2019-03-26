list = ['Google', 'Runoob', 1997, 2000]

#删除列表元素
del list[2]
print("删除列表的元素",list)

#列表长度
print("列表长度",len(list))

L=['Google', 'Runoob', 'Taobao']
print(L[2])
print(L[-2])

#集合
thisset=set(("Google", "Runoob", "Taobao"))
thisset.add("Facebook")
print(thisset)
thisset.remove("Runoob")
print(thisset)
print("集合大小",len(thisset))
#清空集合
thisset.clear()
print(thisset)
