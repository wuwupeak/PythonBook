# 不使用列表拼接的传统做法
listOne = [1, 2, 3, 4, 5]
listTwo = [6, 7, 8, 9, 10]
for value in listTwo:
        listOne.append(value)
print(listOne)

# 使用+号进行列表拼接
listOne = [1, 2, 3, 4, 5]
listTwo = [6, 7, 8, 9, 10]
listOne = listOne + listTwo
print(listOne)
