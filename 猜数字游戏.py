#Author:黄国栋
import random

count=0
num1 = random.randint(0, 101)
print(num1)
while count<3:
    num = int(input("请输入1-100的数字"))
    if num>=0 and num<=100:
        if num>num1:
            print("大于")
        elif num<num1:
            print("小于")
        else:
            print("恭喜您猜对了")
            break
    else:
        print("哈哈")
    count+=1