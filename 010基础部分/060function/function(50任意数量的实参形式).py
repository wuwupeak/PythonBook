# 任意数量的实参-元祖
def print_peoples(*peoples):
        for people in peoples:
                print(people)
print_peoples('people01')
print_peoples('people01', 'people02', 'people03', 'people04', 'people05', 'people06', 'people07', 'people08','people09', 'people10')


##单个参数与多个参数的混合使用
# def print_info(gender,*peoples):
#         print('性别是' + gender + '性的同学如下：')
#         for people in peoples:
#                 print(people)
# print_info('女','people01', 'people02', 'people03')
# print_info('男','people04', 'people05', 'people06', 'people07', 'people08','people09', 'people10')