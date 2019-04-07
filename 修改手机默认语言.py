class Phone:
    def __init__(self,language):
        self.language="英文";

    def update(self,language):
        print("智能手机的默认语言为"+self.language)
        print("将智能手机的默认语言设置为"+language)

p=Phone(None)
p.update("中文")