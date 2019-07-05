# 1.4 分词清洗的精简版本
import re  #导入正则表达式处理模块re
text = input('请输入一串文本：') #输入要清洗的文本
#[',\",\,,:, ,]* 去除" ' : 及空格，*号表示匹配0个或者多个
wordRE = re.compile(r"[',\",\,,:, ,]*([a-z]{1,20})")
matchObject = re.match(wordRE,text)
if matchObject:
        print('清理前的分词为：' + text)
        print('清理后的分词为：' + matchObject.group(1))
else:
        print('无法进行分词匹配！！！')