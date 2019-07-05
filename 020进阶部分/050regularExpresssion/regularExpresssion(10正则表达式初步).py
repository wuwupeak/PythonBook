# 1.1 正则表达式的模块导入和基本用法
text = input('请输入一串文本：') #一个判定用户输入有效手机号的例子
if len(text) == 11: #位数必须正确
        try:
                if int(text) > 10000000000 and int(text) < 10000000000: #整数且去除0起头的输入
                        print('您输入了一个有效的电话号码：' + text)
                else:
                        print('您输入了一个无效的电话号码：' + text)
        except:
                print('您输入了一个无效的电话号码：' + text)
else:
        print('您输入了一个无效的电话号码：' + text)


import re  #导入正则表达式处理模块re
text = input('请输入一串文本：') #一个判定用户输入有效手机号的例子
phoneNumberCheckRE = re.compile(r'\d\d\d\d\d\d\d\d\d\d\d') #匹配任意数字，等价于 [0-9]
matchObject = phoneNumberCheckRE.search(text)
if matchObject == None: #没有匹配则对象为none
        print('您输入了一个无效的电话号码：' + text)
else:
        print('您输入了一个有效的电话号码：' + text)