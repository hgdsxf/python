#Author:黄国栋

#拼接字符串
str1="我今天走了"
num=12345
str2="步"
print(str1+str(num)+str2)

#计算字符串的长度
str3="人生苦短，我用python"
#length=len(str3)
#print("字符串str3的长度为"+length)

#截取字符串
print("截取字符串的第二位",str3[1])
print("从字符串的第六位截取",str3[5:])
print("从左边开始截取到第五位",str3[:5])
print("从第三位到第五位字符",str3[2:5])
print("原字符串",str3)

str4="@黄国栋 @李伦 @卓志刚 @黄国栋"
#分割字符串
list1=str4.split(" ")
for i in list1:
    print(i[1:])
list2=["hgd","ll","zzg"]
#合并字符串
strnew="@".join(list2)
print("合并后字符串为:",strnew)

#检索字符串
print("@黄国栋",str4.count("@黄国栋"),"个")

#find
print(str4.find("@"))

#index===>查询@首次出现的位置
print(str4.index("@"))

#判断字符串是否以@开始
print(str4.startswith('@'))

#判断字符串是否以.com结尾
print("http://www.baidu.com".endswith(".com"))

#字母转换小写字母
print("WWW".lower())

#字母转换大写字母
print("aaaaaaaaaaaa".upper())

#去掉字符串的空格和特殊字符(左右两边的)
print(" hello ###".strip())

#去掉字符串的右边的空格和特殊字符
#print("@AAAA".lsstrip("@"))