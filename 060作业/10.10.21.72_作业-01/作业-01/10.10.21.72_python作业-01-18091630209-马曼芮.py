# """
# Python-作业（第一次）
# 有一段文字需要处理，文字内容如下：
# "When the aerials are down, and your spirit is covered with snows of cynicism and 
# the ice of pessimism, then you are grown old, even at twenty, but as long as your aerials 
# are up, to catch the waves of optimism, there is hope you may die young at eighty."

# """
# 请根据上述文字，编写程序，输出以下问题的结果。

# 问题一：该段文字总共有多少个单词？【4分，其中注释清晰1分】
# 输出格式为"这段话总共有**个单词。"
wordName = "When the aerials are down, and your spirit is covered with snows of cynicism and the ice of pessimism, then you are grown old, even at twenty, but as long as your aerials are up, to catch the waves of optimism, there is hope you may die young at eighty."
wordList = wordName.split()        #    用split内置函数将该段文字分裂成多个字符串组成的列表
wordNumber1 = len(wordList)        #  用len计算列表长度
print("这段话总共有" + str(wordNumber1) + "个单词。")


# 问题二：该段文字总共出现了多少个独一无二的单词？【2分，其中注释清晰1分】
# 输出格式为"这段话总共有**个独一无二的单词。"
wordUniqueList = []
for word in wordList:        #   遍历wordList列表
    if word not in wordUniqueList:
        wordUniqueList.append(word)    #   向字典列表中添加元素
wordNumber2 = len(wordUniqueList)
print("这段话总共有" + str(wordNumber2) + "个独一无二的单词。")




# 问题三：该段文字每个单词出现的次数是多少？【3分，其中注释清晰1分】
# 输出格式为"***在文章中出现的次数是:*"
for word in wordUniqueList:    #    遍历wordUniqueList列表
    wordCount = wordName.count(word)    #  用count内置函数计算列表中元素出现的个数
    print(word + "在文章中出现的次数是：" + str(wordCount))





# """
# 注：
# 提交的文件名称请使用原文件名加学号姓名的方式。【1分】
# 如同学的学号为“00001”，姓名为“张三”
# 提交的文件名为“python-作业-01-00001-张三.py”（注意中间的横杠为英文且没有空格）
# """
