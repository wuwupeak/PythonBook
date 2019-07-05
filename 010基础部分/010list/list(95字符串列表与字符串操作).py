# 1.1 字符串拼接的低效做法
# 拼接任意不可变序列都会生成一个新的序列对象。
# Python字符串是不可变的。
# 由于不变性，字符串可以作为字典的键或set的元素，因为一旦初始化之后字符串的值就不会改变；
# 另一方面，每当需要修改过的字符串时（即使只是微小的修改），都需要创建一个全新的字符串实例。
namesString = ""
namesList = ['周杰伦', '李健', '谢霆锋', '庾澄庆']
for name in namesList:
    namesString = namesString + name
print(namesString)

# 1.2 字符串拼接的高效方法join
# join()方法速度更快（对于大型列表来说更是如此），并不意味着在所有需要拼接两个字符串的情况下都应该使用这一方法。
# 虽然这是一种广为认可的做法，但并不会提高代码的可读性。可读性是很重要的！
namesList = ['周杰伦', '李健', '谢霆锋', '庾澄庆']
namesString = "".join(namesList)
print(namesString)

# 1.3 使用特定字符作为join字符串连接分隔符
namesList = ['周杰伦', '李健', '谢霆锋', '庾澄庆']
namesString = "-".join(namesList)
print(namesString)

namesList = ['周杰伦', '李健', '谢霆锋', '庾澄庆']
namesString = ",".join(namesList)
print(namesString)

# 1.4 使用split()将字符串拆分成字符串列表
words = "My name is Simon"
wordsList = words.split()
print(wordsList)

words = '''你好,
吃饭了没？
没吃的话一起去吃饭？
我在教学楼的。'''
wordsList = words.split()
print(wordsList)
wordsList = words.split('\n')
print(wordsList)

dateTime = "2019-01-8-14-33"
wordsList = dateTime.split('-')
print(wordsList)