"""
Python-作业（第一次）
有一段文字需要处理，文字内容如下：
"When the aerials are down, and your spirit is covered with snows of cynicism and 
the ice of pessimism, then you are grown old, even at twenty, but as long as your aerials 
are up, to catch the waves of optimism, there is hope you may die young at eighty."

"""
text = """
"When the aerials are down, and your spirit is covered with snows of cynicism and 
the ice of pessimism, then you are grown old, even at twenty, but as long as your aerials 
are up, to catch the waves of optimism, there is hope you may die young at eighty."
"""
# 请根据上述文字，编写程序，输出以下问题的结果。

# 问题一：该段文字总共有多少个单词？【4分，其中注释清晰1分】
# 输出格式为"这段话总共有**个单词。"

# 标准化字符串
symbolslist = ["'",'"',"\n","\r","\t",".","_"] #创建符号列表
for symbols in symbolslist: #判断符号是否在文本中
        if symbols in text:
                text = text.replace(symbols,"") #符号在文本中 用空替换掉
text = text.lower() #字符串转换为小写
# 分割字符串
wordlist = text.split(" ") #用空格拆分字符串
wordnumber = len(wordlist) #len


#输出结果
print("这段话总共有" + str(wordnumber) + "个单词")

# 问题二：该段文字总共出现了多少个独一无二的单词？【2分，其中注释清晰1分】
# 输出格式为"这段话总共有**个独一无二的单词。"
newwordlist = []
for word in wordlist: #遍历wordlist
    if word not in newwordlist: #判断不在元素newwordlist 执行语句
        newwordlist.append(word) #添加 元素到 newwordlist
newwordnumber = len(newwordlist) #len函数
#输出结果
print("这段话总共有" + str(newwordnumber) + "个独一无二的单词") 

# 问题三：该段文字每个单词出现的次数是多少？【3分，其中注释清晰1分】
# 输出格式为"***在文章中出现的次数是:*"

for word in newwordlist:  #便利 newwordlist
    wordsnumber = wordlist.count(word) #利用count方法统计词频
    print( word + "在文章中出现的次数是:" + str(wordsnumber))
    

"""

注：
提交的文件名称请使用原文件名加学号姓名的方式。【1分】
如同学的学号为“00001”，姓名为“张三”
提交的文件名为“python-作业-01-00001-张三.py”（注意中间的横杠为英文且没有空格）
"""
