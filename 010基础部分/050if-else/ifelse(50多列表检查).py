# 多列表判定
peoplesOne = ['people01', 'people02', 'people03', 'people04', 'people05', 'people06', 'people07', 'people08','people09', 'people10']
peoplesTwo = ['people01', 'people02', 'people03', 'people04', 'people05']

for peopleOne in peoplesOne:
        if peopleOne in peoplesTwo:
                print(peopleOne+'在两个列表中都存在')
        else:
                print(peopleOne+'仅在peopleOne列表中存在')