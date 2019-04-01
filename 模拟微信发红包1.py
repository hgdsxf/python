import random
money=100
for i in range(1,3):
    a=random.randint(1,money)
    money=money-a;
    print(i,a,money)