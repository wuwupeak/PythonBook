# while循环处理列表
#for 循环是一种遍历列表的有效方式， 但在for 循环中不应修改列表，
# 否则将导致Python难以跟踪其中的元素。
# 要在遍历列表的同时对其进行修改，可使用while 循环。
# 通过将while 循环同列表和字典结合起来使用，可收集、存储并组织大量输入，供以后查看和显示。
peoplesForCheck = ['people01', 'people02', 'people03', 'people04', 'people05', 'people06', 'people07', 'people08','people09', 'people10']
peoplesChecked = []
while peoplesForCheck:
        people = peoplesForCheck.pop()
        print('目前在检查的用户是:' + people.title())
        peoplesChecked.append(people)
print(peoplesChecked)