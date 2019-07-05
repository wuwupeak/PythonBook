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

# 将文字中的","与“。”变为空格。
word = "When the aerials are down, and your spirit is covered with snows of cynicism and"
word = word + " the ice of pessimism, then you are grown old, even at twenty, but as long as your aerials "
word = word + "are up, to catch the waves of optimism, there is hope you may die young at eighty."
wordList = []
wordList = word.replace(",","")
wordList = wordList.replace(".","")
# 拆分单词进入列表中。
wordList = word.split()
number = len(wordList)
print("这段话总共有" + str(number) + "个单词")




# 问题二：该段文字总共出现了多少个独一无二的单词？【2分，其中注释清晰1分】
# 输出格式为"这段话总共有**个独一无二的单词。"

# 新建一个列表并将上一个列表与之对应，找出独一无二的并计算个数。
wordListTwo=[]
for element in wordList:
    if element not in wordListTwo:
        wordListTwo.append(element)
number = len(wordListTwo)
print("这段话总共有" + str(number) + "个独一无二的单词")


# 问题三：该段文字每个单词出现的次数是多少？【3分，其中注释清晰1分】
# 输出格式为"***在文章中出现的次数是:*"

# 在wordListTwo列表中循环。
wordFrequency = []
for wordelement in wordListTwo:
    wordnumber = 0
    # 在wordList列表中循环并与wordListTwo列表对应。
    for element in wordList:
        if element == wordelement:
            wordnumber = wordnumber + 1
            frequency = element + "在文章中出现的次数是:" + str(wordnumber)
    wordFrequency.append(frequency)
print(wordFrequency)
    
        
        





"""
注：
提交的文件名称请使用原文件名加学号姓名的方式。【1分】
如同学的学号为“00001”，姓名为“张三”
提交的文件名为“python-作业-01-00001-张三.py”（注意中间的横杠为英文且没有空格）
"""
