# 函数的闭包，创建形式相似的函数
# Y = aX+b
def functionDef(a,b,x): #三个参数
        return a*x+b
print(str(functionDef(2,5,5)))

def functionUpDef(a,b):
        def functionRun(x): #一个函数和它的环境变量合在一起，就构成了一个闭包（Closure）。a，b就是函数functionRun的环境变量
                return a*x+b
        return functionRun

funcRun = functionUpDef(2,5)
print(str(funcRun(5)))
print(str(funcRun(6)))
