# 1.2 更加精确的电话匹配
import re  #导入正则表达式处理模块re
text = input('请输入一串文本：') #一个判定用户输入有效手机号的例子
phoneNumberCheckRE = re.compile(r'[1][35]\d{9}') #第一位1可以匹配，第二位3或者5可以匹配，也可以使用'[1][35]\d{9}'
matchObject = re.match(phoneNumberCheckRE,text)
# phoneNumberCheckRE.search(text)
if matchObject: #没有匹配则对象为none
        print('您输入了一个有效的电话号码：' + matchObject.group(0)) #不填写参数时，返回group(0)；没有截获字符串的组返回None；截获了多次的组返回最后一次截获的子串。
else:
        print('您输入了一个无效的电话号码：' + text)
