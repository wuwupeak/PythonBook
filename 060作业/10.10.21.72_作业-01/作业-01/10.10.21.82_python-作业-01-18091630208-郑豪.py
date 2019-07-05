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


txt = "When the aerials are down, and your spirit is covered with snows of cynicism and
the ice of pessimism, then you are grown old, even at twenty, but as long as your aerials 
are up, to catch the waves of optimism, there is hope you may die young at eighty."

txt_ls = txt.split()
word_ls = []

symbo1 = [",","."]

for word in txt_ls
    word1 = word.lower()
    word_ls.append(word1)
    


for word in words:
    if symbo1 in words:
        words = txt.replace(1,"")


# print(words)

# 问题二：该段文字总共出现了多少个独一无二的单词？【2分，其中注释清晰1分】
# 输出格式为"这段话总共有**个独一无二的单词。"


word_dic_ls =[]

for word in word_ls:
    if word not in word_dic_ls:
        word_dic_ls.append(word)

word_dic_count = len(word_dic_ls)

print("这段话总共有{}个独一无二的单词。"format（word_dic_count))



# 问题三：该段文字每个单词出现的次数是多少？【3分，其中注释清晰1分】
# 输出格式为"***在文章中出现的次数是:*"

count_ls = []

for word in word_dic_ls:
    count = word_ls.count(word)
    count_ls.append(count)


for index in range(word_dic_count):
    word =word_dic_ls[index]
    word_count = count_ls[index]
    print("{}在文章中出现的此次数是：{}".format(word,word_count))
    


"""
注：
提交的文件名称请使用原文件名加学号姓名的方式。【1分】
如同学的学号为“00001”，姓名为“张三”
提交的文件名为“python-作业-01-00001-张三.py”（注意中间的横杠为英文且没有空格）
"""


