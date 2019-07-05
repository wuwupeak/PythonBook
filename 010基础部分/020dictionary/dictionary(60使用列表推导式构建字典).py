#使用列表推导式构建字典
names = ['高等数学','计算机网络基础','大学英语','Python编程基础','Linux操作系统基础']
scores = [78,85,87,90,76]
nameScoreDic = dict([(name,score) for name in names for score in scores]) #生成方式有问题
print(nameScoreDic)
nameScoreSet = [(name,score) for name in names for score in scores]
print(nameScoreSet)

#使用列表推导式构建字典
names = ['高等数学','计算机网络基础','大学英语','Python编程基础','Linux操作系统基础']
scores = ['一班','二班','三班','四班','五班']
# scores = [78,85,87,90,76]
nameScores = dict([(name,score) for name in names for score in scores]) #生成方式有问题
print(nameScores)

#使用列表推导式快速更换键值
nameClassDic = {'高等数学': '一班', '计算机网络基础': '二班', '大学英语': '三班', 'Python编程基础': '四班', 'Linux操作系统基础': '五班'}
classNameDic = {v:k for k,v in nameClassDic.items()}
print(classNameDic)

#使用列表推导式构建单词和长度的字典
words = ['python','java','c#','sql']
wordsLengthDic = {word : len(word) for word in words}
print(wordsLengthDic)