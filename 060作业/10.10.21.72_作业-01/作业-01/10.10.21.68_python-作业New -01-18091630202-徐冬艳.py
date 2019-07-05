"""
Python-作业（第一次）
有一段文字需要处理，文字内容如下：
"When the aerials are down, and your spirit is covered with snows of cynicism and 
the ice of pessimism, then you are grown old, even at twenty, but as long as your aerials 
are up, to catch the waves of optimism, there is hope you may die young at eighty."

"""
word="""
"When the aerials are down, and your spirit is covered with snows of cynicism and 
the ice of pessimism, then you are grown old, even at twenty, but as long as your aerials 
are up, to catch the waves of optimism, there is hope you may die young at eighty."
"""
# 请根据上述文字，编写程序，输出以下问题的结果。

# 问题一：该段文字总共有多少个单词？【4分，其中注释清晰1分】
word=word.replace(",","")
word=word.replace(".","")
word=word.replace('"',"")
word=word.replace('\n',"")
word=word.replace('"',"")
print(word)
wordlist=[]
wordlist=word.split(" ")#用空格拆分字符串
wordnumber=len(wordlist)#len
print("这段话总共有"+str(wordnumber)+"个单词")

# 输出格式为"这段话总共有**个单词。"







# 问题二：该段文字总共出现了多少个独一无二的单词？【2分，其中注释清晰1分】
newwordlist=[]
for var in wordlist:#遍历wordlist
    if var not in newwordlist:#判断不在元素newwordlist
        newwordlist.append(var)#添加元素到newwordlist
newwordnumber=len(newwordlist)#len函数
print("这段话总共有"+str(newwordnumber)+"个独一无二的单词")
# 输出格式为"这段话总共有**个独一无二的单词。"





# 问题三：该段文字每个单词出现的次数是多少？【3分，其中注释清晰1分】
for var in newwordlist:#遍历newwordlist
    wordsnumber=wordlist.count(var)#利用count统计次数
    print(word+"在文章中出现的次数是:"+str(wordsnumber))
# 输出格式为"***在文章中出现的次数是:*"






"""
注：
提交的文件名称请使用原文件名加学号姓名的方式。【1分】
如同学的学号为“00001”，姓名为“张三”
提交的文件名为“python-作业-01-00001-张三.py”（注意中间的横杠为英文且没有空格）
"""
