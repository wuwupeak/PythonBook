#1.1局部变量和全局变量的错误示例
def judge(value):
        if value == "全局变量":
                localValue = "全局变量"#处于局部作用域的变量，被称为“局部变量”。
        else:
                localValue = "局部变量"
        return localValue
        
globalValue = "全局变量" #处于全局作用域的变量，被称为“全局变量”。
result = judge(globalValue)
print(result)
# print(localValue) #局部变量不能在全局作用域内使用
#一个变量必是其中一种，不能既是局部的又是全局的。
#在被调用函数内赋值的变元和变量，处于该函数的“局部作用域”。

#1.2 global语句
def judge(value):
        global localValue
        if value == "全局变量":
                localValue = "全局变量"#处于局部作用域的变量，被称为“局部变量”。
        else:
                localValue = "局部变量"
        return localValue
globalValue = "全局变量" #处于全局作用域的变量，被称为“全局变量”。
result = judge(globalValue)
print(result)
print(localValue)
#如果需要在一个函数内修改全局变量，就使用global语句。
#如果在函数的顶部有global localValue这样的代码，它就告诉Python，
#在这个函数中，localValue指的是全局变量，所以不要用这个名字创建一个局部变量

# 有4条法则，来区分一个变量是处于局部作用域还是全局作用域：
# 1．如果变量在全局作用域中使用（即在所有函数之外），它就总是全局变量。
# 2．如果在一个函数中，有针对该变量的global语句，它就是全局变量。
# 3．否则，如果该变量用于函数中的赋值语句，它就是局部变量。
# 4．但是，如果该变量没有用在赋值语句中，它就是全局变量。