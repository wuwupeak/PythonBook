# while的continue
peoplesForCheck = ['people01', 'people02', 'women03', 'people04', 'people05', 'women06', 'people07', 'people08','people09', 'people10']
womenChecked = []
while peoplesForCheck:
        people = peoplesForCheck.pop()
        if people[:6] == 'people':
                continue #直接跳到循环体开始，不再执行循环体中continue后面的语句
        # else:
        print('目前在检查的女性用户是:' + people.title())
        womenChecked.append(people)
print(womenChecked)


#1.2 while的break
password = 'pass'
while True:
        passwordInput = input('请输入密码:')
        if passwordInput == password:
                print('密码正确。')
                break
print('你已成功进入系统')
