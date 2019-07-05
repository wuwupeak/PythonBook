# # 1.3 座机号的匹配
import re  #导入正则表达式处理模块re
# text = input('请输入一串文本：') #一个判定用户输入有效手机号的例子
# # \(?  ?表示括号可有可无
# # (0\d{2,3})  0**或0***,括号代表第一个匹配分组
# # [), ,-]  表示')'、'-'、' '都是作为分隔符的匹配
# # (\d{7,8})  7位或8位的号码
# phoneNumberCheckRE = re.compile(r"\(?(0\d{2,3})[), ,-](\d{7,8})") #使用括号进行分组，第一个括号内的为group(1)，以此类推
# matchObject = re.match(phoneNumberCheckRE,text)
# # phoneNumberCheckRE.search(text)
# if matchObject: #没有匹配则对象为none
#         print('您输入了一个有效的座机号码：' + matchObject.group(0))#不填写参数时，返回group(0)；没有截获字符串的组返回None；截获了多次的组返回最后一次截获的子串。
#         print('您输入的区号是：'+matchObject.group(1))
#         print('您输入的电话号码是：'+matchObject.group(2))
# else:
#         print('您输入了一个无效的电话号码：' + text)

# cellValueRE = re.compile(r"(\d{1,2,3})(.*)")

cellValueRE = re.compile(r"(^\d+)") # 字符串以数字开始作为匹配项

cellValue = '12334 中国12社会科3434343学999'
matchObject = re.match(cellValueRE,cellValue)
if matchObject:
        if matchObject.group(1):
                print(matchObject.group(1))

cellValueRE = re.compile(r"\d+$") # 字符串以数字结束作为匹配项
numbers =  cellValueRE.findall(cellValue) #使用每一个匹配项作为列表的元素
print(numbers)