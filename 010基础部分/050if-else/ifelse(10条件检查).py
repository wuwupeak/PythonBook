# 基本的状态检查
peoples = ['people10', 'people02', 'people03', 'people04', 'people05', 'people06', 'people07', 'people08','people09', 'people01']
for people in sorted(peoples):
        if people == 'people02'.lower(): #等于
                print(people.upper())
        else:
                print(people.title())

peoples = ['people10', 'people02', 'people03', 'people04', 'people05', 'people06', 'people07', 'people08','people09', 'people01']
for people in sorted(peoples):
        if people != 'people02'.lower(): #不等于
                print(people.upper())
        else:
                print(people.title())