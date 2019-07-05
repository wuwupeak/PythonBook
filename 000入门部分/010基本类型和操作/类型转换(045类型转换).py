# 1.1 整数类型转字符串类型
age = 45
wordsBegin = "I am "
wordsEnd = " years old."
# 想输出"I am 45 years old."，使用 wordsBegin + 45 + wordsEnd会报错
sentence = wordsBegin + str(age) + wordsEnd
print(sentence)
# str()、int()和float()函数将分别求值为传入值的字符串、整数和浮点数形式。

# 1.2 字符串类型转整数类型
age = "45"
afterYears = 10
ageResult = int(age) + 10
sentence = 'After 10 years, ' + wordsBegin + str(ageResult) + wordsEnd
print(sentence)
print('After 10 years, ' + wordsBegin + str(int(age) + 10) + wordsEnd)
# str()、int()和float()函数将分别求值为传入值的字符串、整数和浮点数形式。