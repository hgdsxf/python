#算术运算符
a=5
b=2

print("加",a+b)
print(a-b)
print(a**b)
print(a%b)
print(a/b)
print(a//b)
print(a*b)

print("------------------------------")

#比较运算符
a=5
b=3
c=1

if a==b:
    print("ab相等")
else:
    print("ab不相等")

if a!=b:
    print("ab不相等")
else:
    print("ab相等")

if a<b:
    print("a小于b")
else:
    print("a大于b")

if a>b:
    print("a大于b")
else:
    print("a小于b")

if a<=b:
    print("a小于等于b")
else:
    print("a大于等于b")

if a>=b:
    print("a大于等于b")
else:
    print("a小于等于b")

print("------------------------")

#赋值运算符
a=2
b=2
c=5

c+=b
print(c)

c-=b
print(c)

c*=b
print(c)

c/=b
print(c)

c%=b
print(c)

c**=b
print(c)

c//=b
print(c)

print("----------------------------------------")
#成员运算符
a=10
b=2
list=[1,2,3,4,5]

if a in list:
    print("a在list")
else:
    print("a不在list")

if b not in list:
    print("b不在list")
else:
    print("b在list")

#身份运算符
