# 对字符串每个字母的遍历
valueString = 'Hello, world!'  # 注意空格也是一个字符
for value in valueString:
        print(value)

valueString = '来啦老弟'  # 注意空格也是一个字符
for value in valueString:
        print(value)

# 字符串拆分函数和字符串列表
valueString = """
The Thematic-Forum on Think Tank Exchanges was held by the Publicity Department of the CPC Central Committee. 
More than 300 think tank and media representatives from over 60 countries and regions attended the forum.
"""
print(valueString)
wordsList = valueString.split()   # split()通过指定分隔符对字符串分割 
print(wordsList)

wordsList = valueString.split(' ', 1)   # split()通过指定分隔符对字符串分割，如果参数 num 有指定值，则仅分隔 num+1 个子字符串 
print(wordsList)

# 如何处理掉分割元素中的其他字符
valueString = """
The Thematic-Forum on Think Tank Exchanges was held by the Publicity Department of the CPC Central Committee. 
More than 300 think tank and media representatives from over 60 countries and regions attended the forum.
"""
wordsList = valueString.split()
for index in range(len(wordsList)):
        wordsList[index] = wordsList[index].strip('.')  # strip()用于移除字符串头尾指定的字符（默认为空格）或字符序列。注意：该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。
print(wordsList)        


valueString = valueString.replace('.', '')  # replace() 把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次。
wordsList = valueString.split()
print(wordsList)

valueString = valueString.lower()  # lower()、upper()用来将字符串转换为小写、大写字符串
wordsList = valueString.split()
print(wordsList)

# 将字符串列表按照一个规则拼接为一个字符串
valueString = ""
for word in wordsList:
        valueString = valueString + word + "-"
print(valueString)
valueString = valueString.strip("-")
print(valueString)

# join()方法速度更快（对于大型列表来说更是如此），并不意味着在所有需要拼接两个字符串的情况下都应该使用这一方法。
# 虽然这是一种广为认可的做法，但并不会提高代码的可读性。可读性是很重要的！
valueString = ""
valueString = "-".join(wordsList)
print(valueString)
