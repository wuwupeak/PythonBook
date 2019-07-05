"""
Python-作业（第一次）
有一段文字需要处理，文字内容如下：
"When the aerials are down, and your spirit is covered with snows of cynicism and 
the ice of pessimism, then you are grown old, even at twenty, but as long as your aerials 
are up, to catch the waves of optimism, there is hope you may die young at eighty."

"""
# 请根据上述文字，编写程序，输出以下问题的结果。

# 问题一：该段文字每个单词出现的次数是多少？【3分，其中注释清晰1分,必须用字典输出】
# 输出格式为"{***:***,***:***}"
# 要处理的文本
txt = """ When the aerials are down, and your spirit is covered with snows of cynicism  
and the ice of pessimism, then you are grown old, even at twenty, but as long as your aerials 
are up, to catch the waves of optimism, there is hope you may die young at eighty."""
# 创建需转换的符号列表
symp = [',', '.']
# 符号转换
for i in symp:
    txt = txt.replace(i, "")
# print(txt)
# 单词小写化
txt = txt.lower()
# 单词分割
word_ls = txt.split()
# 消除重复元素
word_set = set(word_ls)
# 创建单词字典列表
word_dic_ls = list(word_set)
# 创建单词计数字典
word_count_dic = {}
for word in word_dic_ls:
    # 计算单词在文章中出现的次数
    count = word_ls.count(word)
    word_count_dic[word] = count

print(word_count_dic)


# 问题二：其中单词长度超过5个字母的单词出现的次数是多少？【2分，其中注释清晰1分,必须用字典输出】
# 输出格式为"{***:***,***:***}"
# 创建单词长度超过5的字典
more_than_5 = {}
# for word in word_dic_ls:
#     # 计算单词长度
#     lengh = len(word)
#     if lengh > 5:
#         # 计算长度大于5的单词在文章中出现的次数
#         count = word_ls.count(word)
#         more_than_5[word] = count
for key, value in word_count_dic.items():
    # 计算字典中键(单词)的长度
    length = len(key)
    if length > 5:
        more_than_5[key] = value
print(more_than_5)


# 问题三：设计一个交互式程序，能够根据用户输入的单词将单词出现的次数打印在屏幕上？【3分，其中注释清晰1分】
# 输出格式为"***在文章中出现的次数是:*"
# 获取用户输入的单词
word = input("请输入文章中的单词:")
# 获取用户输入的单词在文章中出现的次数
word_count = word_count_dic.get(word, 0)
print("{}在文章中出现的次数是:{}".format(word, word_count))


"""
注：
提交的文件名称请使用原文件名加学号姓名的方式。【1分】
如同学的学号为“00001”，姓名为“张三”
提交的文件名为“python-作业-02-00001-张三.py”（注意中间的横杠为英文且没有空格）
"""
