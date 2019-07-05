# age = input('请输入您的年龄：')
# wordBegin = '你输入的年龄是'
# wordEnd = '岁。'

# ageInt = int(age)
# ageAdd = ageInt + 10

# ageInfo = wordBegin + age + wordEnd
# ageAddInfo = '过去10年以后' + str(ageAdd) + wordEnd

# print(ageInfo)
# print(ageAddInfo)


# age = input('请输入您的年龄：')
# yearsAdd = input('请输入过去的年份：')
# wordBegin = '你输入的年龄是'
# wordEnd = '岁。'

# ageInt = int(age)
# ageAdd = ageInt + int(yearsAdd)

# ageInfo = wordBegin + age + wordEnd
# ageAddInfo = '过去' + yearsAdd + '年以后' + str(ageAdd) + wordEnd

# print(ageInfo)
# print(ageAddInfo)

# result = True
# print(result)
# print(2>3)

# age = input('请输入您的年龄：')
# ageInt = int(age)
# if ageInt > 80:
#     print('您输入的年龄是不合法的')
# elif ageInt > 30:
#     print('您输入的年龄有点大')
# elif ageInt < 15:
#     print('您输入的年龄有点小')
# else:
#     print('您输入的年龄是合法的')


# age = input('请输入您的年龄：')
# ageInt = int(age)
# if (ageInt > 15) and (ageInt < 30):
#     print('您输入的年龄是合法的')
# else:
#     print('您输入的年龄是不合法的')

# age = input('请输入您的年龄：')
# ageInt = int(age)
# if (ageInt < 15) or (ageInt > 30) or (ageInt == 15) or (ageInt == 30):
# #if (ageInt <= 15) or (ageInt >= 30):
#     print('您输入的年龄是不合法的')
# else:
#     yearsAdd = input('请输入过去的年份：')
#     wordBegin = '你输入的年龄是'
#     wordEnd = '岁。'

#     ageInt = int(age)
#     ageAdd = ageInt + int(yearsAdd)

#     ageInfo = wordBegin + age + wordEnd
#     ageAddInfo = '过去' + yearsAdd + '年以后' + str(ageAdd) + wordEnd

#     print(ageInfo)
#     print(ageAddInfo)
 




age = input('请输入您的年龄：')
ageInt = int(age)
if (ageInt < 15) or (ageInt > 30) or (ageInt == 15) or (ageInt == 30):
#if (ageInt <= 15) or (ageInt >= 30):
    print('您输入的年龄是不合法的')
else:
    yearsAdd = input('请输入过去的年份：')

    ageInt = int(age)
    ageAdd = ageInt + int(yearsAdd)
    if ageAdd > 100:
        print("你输的年份太大了，超过了100岁")
    else:
        wordBegin = '你输入的年龄是'
        wordEnd = '岁。'

        ageInfo = wordBegin + age + wordEnd
        ageAddInfo = '过去' + yearsAdd + '年以后' + str(ageAdd) + wordEnd

        print(ageInfo)
        print(ageAddInfo)