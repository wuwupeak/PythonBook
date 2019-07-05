# while 限定次数的循环
count = 1
while count<=5:
        print('这是循环的第' + str(count) + '次')
        count += 1

count = 1
active = True
while active:
        print('这是循环的第' + str(count) + '次')
        count += 1
        if count == 6:
                active = False #使用while循环内的状态位进行控制

count = 1
active = True
while active:
        print('这是循环的第' + str(count) + '次')
        if count == 5:
                active = False #使用while循环内的状态位进行控制
        count += 1

for value in range(1,6): #使用for循环
        print('这是循环的第' + str(value) + '次')