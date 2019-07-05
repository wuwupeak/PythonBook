#1.1 生成器(generator)和列表推导式(comprehensions)的差异
listFromComprehension = [x*x for x in range(10)] #使用[]代表列表推导式
print(listFromComprehension)

#如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
#这样就不必创建完整的list，从而节省大量的空间。
listFromGenerator = (x*x for x in range(10)) #使用()代表生成器
for element in listFromGenerator:
    print(element)

#1.2 斐波拉契数列(Fibonacci)的实现

#传统实现
def Fibonacci(max):
    count, a, b = 0, 0, 1
    while count < max:
        print(b)
        a, b = b, a+b
        count = count + 1
Fibonacci(6)

#生成器实现
def Fibonacci():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a+b
fib = Fibonacci()
listFib = [next(fib) for i in range (6)]
print(listFib)
