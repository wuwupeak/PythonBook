import function_60_forImport as peopleFunction #导入模块使用别名

# 1.1 基本的函数定义
peopleFunction.printName('张三')

peopleFunction.sumTwo(1,2)
peopleFunction.sumTwo(1.1,2.1)
peopleFunction.sumTwo('123','456')

# 1.2 位置实参的顺序
peopleFunction.printInfo('张三','男')
peopleFunction.printInfo('男','张三') #实参顺序错误
peopleFunction.printInfo(gender = '男',name = '张三') #关键字实参

# 1.3 形参的默认值
peopleFunction.printUserInfo('张三')
peopleFunction.printUserInfo('李丽','女')

# 1.4 返回值
fullName = peopleFunction.get_fullName('张','三')
print(fullName)


fullName = peopleFunction.get_name('张','三')
print(fullName)
fullName = peopleFunction.get_name('张','三','贵')
print(fullName)

# 1.5 任意数量的实参-元祖
peopleFunction.print_peoples('people01')
peopleFunction.print_peoples('people01', 'people02', 'people03', 'people04', 'people05', 'people06', 'people07', 'people08','people09', 'people10')


peopleFunction.print_info('女','people01', 'people02', 'people03')
peopleFunction.print_info('男','people04', 'people05', 'people06', 'people07', 'people08','people09', 'people10')

# 1.6 任意数量的关键字实参-字典
userInfo =  peopleFunction.build_info(身高 = '170cm',体重 = '60kg',年龄 = 45)
print(userInfo)

