student={1:'Jack',2:'Bob',3:'Marry',4:'Micle'}

#chaxun
print(student)
print(student[3])

#add
student[5]="AAAAA"
print(student)

#修改字典
student[2]="BBBBB"
print(student)

#删除某一个键值对
del student[1]
print(student)

#清空字典全部内容
student.clear()
print(student)

#删除字典
del student
print(student)
