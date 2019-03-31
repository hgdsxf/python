#Author:黄国栋

import random

title=["python","人生苦短",["爬虫","自动化运维"]]

#删除列表
#del title

#遍历列表
#for item in title:
 #   print(item)

#添加元素
title.append("三星")
title.append("oppo")
title.append("vivo")
title.append("华为")
title.append("华为")
title.append("苹果")
print("添加完成后元素后的列表",title)

#修改元素
title[2]="黄国栋"
print("修改完成后的列表",title)

#删除元素
del title[0]
print("删除元素后的列表",title)

#获取指定元素坐在列表中出现的次数
#num=title.count("华为")
#print("获取华为在列表中出现的次数",num)

#获取指定元素在列表中出现的下标
#num1=title.index["华为"]
#print("获取华为在列表首次出现的下标",num1)

grade=[89,67,89,80,34]
sum1=sum(grade)
print("对列表进行求和",sum1)
print("原列表",grade)
grade.sort()
print("升序",grade)
grade.sort(reverse=True)
print("降序",grade)


arr=[]
for i in range(4):
    arr.append([])
    for j in range(5):
        arr[i].append(j)
        #print(i)
print("列表arr",arr)
