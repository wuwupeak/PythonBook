# 如需要输出这样的句子"我是学生"的英语为：I'm student.
# "我是学生"的英语为：I'm student.

# 单引号，双引号无论哪一种都无法解决
# print(""我是学生"的英语为：I'm student.")
# print('"我是学生"的英语为：I'm student.')

# 转义字符
# “转义字符”让你输入一些字符，它们用其他方式是不可能放在字符串里的。
# 转义字符包含一个倒斜杠（\），紧跟着是想要添加到字符串中的字符。
# （尽管它包含两个字符，但大家公认它是一个转义字符。）

#  \' 单引号 
#  \" 双引号 
#  \t 制表符 
#  \n 换行符 
#  \\  倒斜杠

print("\"我是学生\"的英语为：I'm student.")
print('"我是学生"的英语为：I\'m student.')

print('\t"我是学生"的英语为：I\'m student.')
print('"我是学生"的英语为：\nI\'m student.')
# 在字符串开始的引号之前加上r，使它成为原始字符串。
print(r"\"我是学生\"的英语为：I'm student.")
print(r'"我是学生"的英语为：I\'m student.')

# 字符串的in和not in操作符
# 用in或not in连接两个字符串得到的表达式，将求值为布尔值True或False。
# 这些表达式测试第一个字符串（精确匹配，区分大小写）是否在第二个字符串中。
print("我是" in "我是学生")
print("我是" not in "我是学生")

# 字符串方法startswith()和endswith()
# 如果它们所调用的字符串以该方法传入的字符串开始或结束，startswith()和endswith()方法返回True。
# 否则，方法返回False。
print("我是学生" .startswith("我是"))
print("我是学生" .endswith("我是"))

# 字符串的大小写方法upper()、lower()
print('Hello world!'.upper())
print('Hello world!'.lower())

# strip()、rstrip()和lstrip()删除空白字符
# strip()字符串方法将返回一个新的字符串，它的开头或末尾都没有空白字符。
# lstrip()和rstrip()方法将相应删除左边或右边的空白字符。
print('   Hello world!    ')
print('   Hello world!    '.strip())
print('   Hello world!    '.rstrip())
print('   Hello world!    '.lstrip())
