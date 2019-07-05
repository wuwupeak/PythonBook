# 列表的值判定
peoples = ['people10', 'people02', 'people03', 'people04', 'people05', 'people06', 'people07', 'people08','people09', 'people01']
if 'people02' in peoples:
        print("'people02'在列表中") #'和"的用法
if 'people11' not in peoples:
        print('"people11"不在列表中') #'和"的用法

# 空列表的判定
peoples = []
if peoples: #列表为空的判定
        print('列表有数据')
else:
        print('列表为空')