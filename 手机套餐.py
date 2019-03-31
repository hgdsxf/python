#Author:黄国栋
print("定制自己的手机套餐:")

print("A.请设置通话时长:")
print("A1.0分钟")
print("A2.50分钟")
print("A3.100分钟")
print("A4.300分钟")
num1=input("输入选择的通话时长编号(A1,A2,A3,A4):")
Tonghua={
    "A1":"0",
    "A2":"50",
    "A3":"100",
    "A4":"300"
}

print("B.请设置流量包:")
print("B1.0M")
print("B2.500M")
print("B3.1G")
print("B4.5G")
num2=input("输入选择的流量包编号(B1,B2,B3,B4):")
liuliangbao={
    "B1": "0M",
    "B2": "500M",
    "B3": "1G",
    "B4": "5G"
}

print("B.请设置短信条数:")
print("C1.0条")
print("C2.50条")
print("C3.100条")
num3=input("输入选择的短信编号(C1,C2,C3):")
duanxin={
    "C1": "0",
    "C2": "50",
    "C3": "100"
}

print("您已经购买好套餐，免费通话时长为"+Tonghua[num1]+"分钟/月，流量为"
                         +liuliangbao[num2]+"/月，短信条数为"
                         +duanxin[num3]+"条/月")