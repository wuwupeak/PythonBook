# 1.5 if 语句的三元运算
peoples = ['people01', 'people02', 'people03', 'people04', 'man05', 'people06', 'people07', 'people08','people09', 'people10']
womens = []
for people in peoples:
        if people[0:6] == 'people':
                womens.append('women' + people[6:])
        else:
                womens.append(people)
print(womens)


peoples = ['people01', 'people02', 'people03', 'people04', 'man05', 'people06', 'people07', 'people08','people09', 'people10']
womens = []
for people in peoples:
        womens.append('women' + people[6:]) if people[0:6] == 'people' else womens.append(people) #if的三元运算
print(womens)

#lamda 表达式对字符串列表的处理
peoples = ['people01', 'people02', 'people03', 'people04', 'man05', 'people06', 'people07', 'people08','people09', 'people10']
tempWomen = list(filter(lambda people:people[0:6] == 'people',peoples))
tempMan = list(filter(lambda people:people[0:6] != 'people',peoples))
womens = list(map(lambda people:'women' + people[6:],tempWomen))+tempMan #字符串列表的追加
print(womens)