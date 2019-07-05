# range的含义
for value in range(1, 10): 
        print(value)

for value in range(10): 
        print(value)

# 使用range创建列表
numbers = list(range(1, 10)) 
print(numbers)
for nuimber in numbers:
        print(nuimber)

# 使用range创建列表,带步长
numbers = list(range(1, 10, 2)) 
print(numbers)

numbers = list(range(2, 11, 2)) 
print(numbers)

# 使用值计算建立列表
numbers = []
for value in range(1, 11): 
        numbers.append(value**2)
print(numbers)

# 列表的统计计算
numbers = list(range(1, 11))
print(min(numbers)) 
print(max(numbers))
print(sum(numbers))
print(sum(numbers)/len(numbers))