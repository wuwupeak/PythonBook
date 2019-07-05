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
# List = "When the aerials are down, and your spirit is covered with snows of cynicism and \
# the ice of pessimism, then you are grown old, even at twenty, but as long as your aerials \
# are up, to catch the waves of optimism, there is hope you may die young at eighty."    # \(转义)
# #空格替换逗号
# # people = List.replace(',','')
# #分割字符串
# wordList = people.split()
# #计算字符数
# print(len(wordList))
# sentence = len(wordList)
# print('这段文字总共有' + str(sentence) + '个单词')



# 问题二：该段文字总共出现了多少个独一无二的单词？【2分，其中注释清晰1分】
# 输出格式为"这段话总共有**个独一无二的单词。"
# wordlist = "When the aerials are down, and your spirit is covered with snows of cynicism and \
# the ice of pessimism, then you are grown old, even at twenty, but as long as your aerials \
# are up, to catch the waves of optimism, there is hope you may die young at eighty."
# newwordlist = []
# for word in wordlist:#遍历wordlist
#     if word not in newwordlist:#判断元素不在newwordlist
#         newwordlist.append(word)#将元素添加到newwordlist
# newwordnumber = len(newwordlist)#len函数
# print('这段话总共有' + str(newwordnumber) + '独一无二的单词')


# 该段文字每个单词出现的次数是多少？
# # 问题三：【3分，其中注释清晰1分】
# # 输出格式为"***在文章中出现的次数是:*"
word = "When the aerials are down, and your spirit is covered with snows of cynicism and the ice of pessimism, then you are grown old, even at twenty, but as long as your aerials are up, to catch the waves of optimism, there is hope you may die young at eighty."
word = word.replace(',','')
word = word.split()
print(word)
setword = set(word)
for i in setword:
    count = word.count(i)
    print(i,'在文章出现的次数',count)


# """
# 注：
# 提交的文件名称请使用原文件名加学号姓名的方式。【1分】
# 如同学的学号为“00001”，姓名为“张三”
# 提交的文件名为“python-作业-01-00001-张三.py”（注意中间的横杠为英文且没有空格）
# """
