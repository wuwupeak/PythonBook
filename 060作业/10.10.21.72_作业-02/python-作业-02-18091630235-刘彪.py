class Text():  # 定义 text类
    def __init__(self, text):
        self.text = text

    def Get(self, symbolslist):  # 定义 Get方法
        content = self.text
        countnumberlist = []
        wordnumberlist = []
        countwordlist = []  
        countdict = {}
        for symbol in symbolslist:
            if symbol in content:
                content.replace(symbol, " ")
        
        wdlist = content.split()
        wordlist = list(set(wdlist))
        for word in wordlist:
            wordnumberlist.append(content.count(word))
        worddict = dict(zip(wordlist, wordnumberlist))

        for key,value in worddict.items():
            if len(key) > 5:
                countdict[key] = value
        
        self.dict = worddict  # 给 Text类 dict 属性赋值
        self.countdict = countdict  # 给 Text类 countdict 属性赋值

    def Getwordcount(self, word):
        self.wordcount = self.dict.get(word)
        if self.wordcount is None:
            self.wordcount = 0
        


symbolslist = ['"', ".", "\n", "\t", "\r", ":", "/"]

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

text = """
"When the aerials are down, and your spirit is covered with snows of cynicism and 
the ice of pessimism, then you are grown old, even at twenty, but as long as your aerials 
are up, to catch the waves of optimism, there is hope you may die young at eighty."
"""

result = Text(text)
result.Get(symbolslist)
print(result.dict)


# 问题二：其中单词长度超过5个字母的单词出现的次数是多少？【2分，其中注释清晰1分,必须用字典输出】
# 输出格式为"{***:***,***:***}"

print(result.countdict)


# 问题三：设计一个交互式程序，能够根据用户输入的单词将单词出现的次数打印在屏幕上？【3分，其中注释清晰1分】
# 输出格式为"***在文章中出现的次数是:*"


word = input("请输入一个单词: ")
result.Getwordcount(word)
print("{}在文章中出现的次数是:{}".format(word,result.wordcount))

"""
注：
提交的文件名称请使用原文件名加学号姓名的方式。【1分】
如同学的学号为“00001”，姓名为“张三”
提交的文件名为“python-作业-02-00001-张三.py”（注意中间的横杠为英文且没有空格）
"""

