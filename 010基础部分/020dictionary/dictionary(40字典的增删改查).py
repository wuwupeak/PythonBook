# 字典键值对的增加
people = {'身高': 170, '体重': 60, '年龄': 45}
people['籍贯'] = '江苏'
people['性别'] = '男'
print(people)

# 字典值的修改
people = {'身高': 170, '体重': 60, '年龄': 45}
people['年龄'] = 40
print(people)

# 字典键值对的删除
people = {'身高': 170, '体重': 60, '年龄': 45}
del people['身高']
print(people)

# 字典键值对的查找
people = {'身高': 170, '体重': 60, '年龄': 45}
age = people.get('年龄')
print(age)


                        

