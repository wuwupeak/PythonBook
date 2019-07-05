# 多条件判定
peoples = ['people10', 'people02', 'people03', 'people04', 'people05', 'people06', 'people07', 'people08','people09', 'people01']
for people in peoples:
        if people == 'people02' or people == 'people01': #多个条件的判定
                print('你选中的是01或者02的用户')
        elif people == 'people10':
                print('你选中的是10的用户') #取消了else的默认操作