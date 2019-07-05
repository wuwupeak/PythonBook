peoples = [{'身高': 170, '体重': 60, '年龄': 45}, {'身高': 180, '体重': 53, '年龄': 23}]
peopleOne = peoples[0]
peopleTwo = peoples[1]
print(peopleOne)
print(peopleTwo)


for people in peoples:
    print(people)
    for key, value in people.items():
        print("键:" + key + ";" + "值：" + str(value))


for people in peoples:
    print(people)
    for key, value in people.items():
        print("键:" + key + ";" + "值：" + str(value))

# 访问字典值
people = {'身高': 180, '体重': 53, '年龄': 23}
print(people['身高'])
print('这个人是：' + str(people['年龄']) + '岁。')

# 检查字典中是否存在键或值
# in和not in操作符可以检查值是否存在于列表中。
# 也可以利用这些操作符，检查某个键或值是否存在于字典中。
people = {'身高': 180, '体重': 53, '年龄': 23}
key = '身高'
judgeResult = key in people.keys()
print(judgeResult)
value = 53
judgeResult = value in people.values()
print(judgeResult)

# get()方法使用键来获取值
# get()方法，它有两个参数：要取得其值的键，以及如果该键不存在时，返回的备用值。
people = {'身高': 180, '体重': 53, '年龄': 23}
key = '身高'
getResult = people.get(key)
print(getResult)

key = '籍贯'
getResult = people.get(key, '没有键值')
print(getResult)