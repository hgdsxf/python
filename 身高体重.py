#Author:黄国栋

height=float(input("请输入您的身高:"))
weight=float(input("请输入您的体重:"))

bmi=weight/(height*height)
print(bmi)
if bmi<18.5:
    print("您的体重过轻")
elif bmi>=18.5 and bmi<24.9:
    print("正常")
elif bmi>=24.9 and bmi<29.9:
    print("超标")
else:
    print("肥胖")