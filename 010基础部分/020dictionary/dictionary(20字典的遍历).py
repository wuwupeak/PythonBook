# 字典键值对的遍历
people = {'身高': 180, '体重': 53, '年龄': 23}
for key,value in people.items():
        print("键：" + key)
        print("值：" + str(value))

# 字典键的遍历
for key in people.keys(): #只遍历键
        print("键：" + key)

# 字典值的遍历
for key in people.values(): #只遍历值
        print("值：" + str(value))