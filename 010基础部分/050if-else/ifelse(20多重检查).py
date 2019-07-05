# 多重判定
peoples = ['people10', 'people02', 'people03', 'people04', 'people05', 'people06', 'people07', 'people08','people09', 'people01']
print(peoples[0][6:8])  #正向截取
print(peoples[0][6:])  #正向截取
print(peoples[0][-2:]) #反向截取
for people in sorted(peoples):
        if int(people[6:8]) >=7:  #数字判定
                print(people.upper())
        elif int(people[6:8]) <= 3:
                print(people.title())
        else:
                print(people.lower())