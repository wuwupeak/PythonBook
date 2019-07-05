"""
Python-作业（第一次）
有一段文字需要处理，文字内容如下：
"When the aerials are down, and your spirit is covered with snows of cynicism and 
the ice of pessimism, then you are grown old, even at twenty, but as long as your aerials 
are up, to catch the waves of optimism, there is hope you may die young at eighty."

"""
# 请根据上述文字，编写程序，输出以下问题的结果。

# 问题一：该段文字最先出现的10个单词，最后出现的10个单词分别是多少？【3分，其中注释清晰1分,必须用字典输出】
# 输出格式为"[***，****，****，****]"
# 输出格式为"[***，****，****，****]"
stringValue = """When the aerials are down, and your spirit is covered with snows of cynicism and 
the ice of pessimism, then you are grown old, even at twenty, but as long as your aerials 
are up, to catch the waves of optimism, there is hope you may die young at eighty."""
stringCleaned = stringValue.replace(",","").replace(".","")
wordsList = stringCleaned.split()
print(wordsList[0:10])
print(wordsList[-10:])




# 问题二：设计一个交互式程序能够获取用户每次敲击回车前输入的英文单词数和字母数量（不含空格）？【6分，其中注释清晰1分,必须用字典输出】
# 输出格式为"输入的单词数量为：****。输入的字母数量为：*****。"

words = input("请输入：")
words = words.replace(","," ")
words = words.replace("."," ")
words = words.replace("'"," ")
wordsList = words.split()
wordsCount = len(wordsList)
print(wordsList)
charCount = 0
for word in wordsList:
        charCount = charCount + len(word)
print("输入的单词数量为：" + str(wordsCount) + "。" + "输入的字母数量为：" + str(charCount) + "。")





"""
注：
提交的文件名称请使用原文件名加学号姓名的方式。【1分】
如同学的学号为“00001”，姓名为“张三”
提交的文件名为“python-作业-03-00001-张三.py”（注意中间的横杠为英文且没有空格）
"""
