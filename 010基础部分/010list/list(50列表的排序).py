# 列表的永久排序和逆排序
peoples = ['people10', 'people02', 'people03', 'people04', 'people05', 'people06', 'people07', 'people08','people09', 'people01']
print(peoples)
peoples.sort()  # 列表的永久排序，升序
print(peoples)
peoples.sort(reverse = True)  # 列表的永久逆排序，降序
print(peoples)

# 列表的临时排序和逆排序
peoples = ['people10', 'people02', 'people03', 'people04', 'people05', 'people06', 'people07', 'people08','people09', 'people01']
print(sorted(peoples))  # 列表的临时排序，升序
print(peoples)
print(sorted(peoples, reverse = True))  # 列表的临时排序，降序
print(peoples)

# 列表的逆序
peoples = ['people10', 'people02', 'people03', 'people04', 'people05', 'people06', 'people07', 'people08','people09', 'people01']
peoples.reverse()  # 列表逆序
print(peoples)