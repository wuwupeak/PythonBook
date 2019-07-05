"""
Python-作业（第一次）
有一段文字需要处理，文字内容如下：
"When the aerials are down, and your spirit is covered with snows of cynicism and 
the ice of pessimism, then you are grown old, even at twenty, but as long as your aerials 
are up, to catch the waves of optimism, there is hope you may die young at eighty."

"""
# 请根据上述文字，编写程序，输出以下问题的结果。

# 问题一：该段文字总共有多少个单词？【4分，其中注释清晰1分】
# 输出格式为"这段话总共有**个单词。"

word = """When the aerials are down, and your spirit is covered with snows of cynicism and 
the ice of pessimism, then you are grown old, even at twenty, but as long as your aerials 
are up, to catch the waves of optimism, there is hope you may die young at eighty."""
word = word.replace(',',' ').replace('.',' ') #去掉句子中的,.
Newword = word.strip() #去掉头尾空格
index = 0
count = 0
while index < len(Newword):
    while Newword[index] !=" ": #有空格时结束当前循环
        index +=1
        if index == len(Newword): #下标与字符串长度相等结束当前循环
            break
    count += 1 #计算单词的个数
    if index == len(Newword): #下标与字符串长度相等结束当前循环
        break
    while Newword[index] == " ": #单词之间多个空格时，下标加一
        index += 1
print("这段话总共有" + str(count) + "个单词")



# 问题二：该段文字总共出现了多少个独一无二的单词？【2分，其中注释清晰1分】
# 输出格式为"这段话总共有**个独一无二的单词。"
word = """When the aerials are down, and your spirit is covered with snows of cynicism and 
the ice of pessimism, then you are grown old, even at twenty, but as long as your aerials 
are up, to catch the waves of optimism, there is hope you may die young at eighty."""
wordList = wordList.replace(',',' ').replace('.',' ') #去掉句子中的,.
wordList = word.split()
wordListTwo = []
for element in wordList:
    if element not in wordListTwo:
        wordListTwo.append(element)
number = len(wordListTwo)
print("这段话总共有" + str(number) + '个独一无二的单词'）




# 问题三：该段文字每个单词出现的次数是多少？【3分，其中注释清晰1分】
# 输出格式为"***在文章中出现的次数是:*"
word = """When the aerials are down, and your spirit is covered with snows of cynicism and 
the ice of pessimism, then you are grown old, even at twenty, but as long as your aerials 
are up, to catch the waves of optimism, there is hope you may die young at eighty."""
word = word.replace(',',' ').replace('.',' ') #去掉句子中的,.
Newword = word.strip() #去掉头尾空格
Newword = word.split() #把空格设为分割符
print(Newword)
setword=set(Newword) 
for i in setword:
    count=Newword.count(i)
    print(i,'在文章中出现的次数是：',count)


"""
注：
提交的文件名称请使用原文件名加学号姓名的方式。【1分】
如同学的学号为“00001”，姓名为“张三”
提交的文件名为“python-作业-01-00001-张三.py”（注意中间的横杠为英文且没有空格）
"""
