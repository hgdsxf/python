#Author:黄国栋
import re
parrent=r'1[3,4,5,7,8]\d{9}'
phone="13788888888"
macth=re.match(parrent,phone)
if macth=="None":
    print(phone,"不是有效的移动号码")
else:
    print(phone, "是有效的移动号码")