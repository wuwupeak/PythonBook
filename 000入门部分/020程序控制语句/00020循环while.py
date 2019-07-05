# while True:
#     print('开始循环了')

loopCount = 1
# while loopCount < 101:
#     print('开始循环了')
#     print(str(loopCount))
#     loopCount = loopCount + 1
# print('我跳出循环了')

# loopActive = True
# while loopActive:
#     age = input('请输入你的年龄：')
#     print('您输入的年龄是：' + age + '岁。')

# loopActive = True
# while loopActive:
#     age = input('请输入你的年龄：')
#     if int(age) == 0:
#         loopActive = False
#         print('程序已经退出了。')
#     else:
#         print('您输入的年龄是：' + age + '岁。')

loopActive = True
while loopActive:
    age = input('请输入你的年龄：')
    if int(age) == 0:
        print('程序已经退出了。')
        break
    ageInt = int(age)
    if ageInt >100:
        print('您输入的年龄大于100岁了!!!')
    else:
        print('您输入的年龄是：' + age + '岁。')



# loopActive = True
# while loopActive:
#     age = input('请输入你的年龄：')
#     if int(age) == 0:
#         print('程序已经退出了。')
#         break
#     ageInt = int(age)
#     if ageInt >100:
#         print('您输入的年龄大于100岁了!!!')
#         continue
#     print('您输入的年龄是：' + age + '岁。')
