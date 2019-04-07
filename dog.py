class Dog():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sit(self):
        print(self.name+"登下")
    def dagun(self):
        print(self.name+"打滚")

d=Dog("小白",3)
d.sit()
d.dagun()
