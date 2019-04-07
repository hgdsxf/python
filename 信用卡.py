class Creditcard:

    #构造方法
    def __init__(self,card,password):
        self.card=card
        self.password="123456"

    def updata(self,password):
        print("信用卡"+self.card+"默认密码是"+self.password)
        print("信用卡"+self.card+"的密码是"+password)

c=Creditcard("45645215645414424",None)
c.updata("654321")
