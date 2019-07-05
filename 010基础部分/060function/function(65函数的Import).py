# 函数的import
import function_60_forImport

# 函数包使用
function_60_forImport.printName('张三')
function_60_forImport.sumTwo(1,2)
function_60_forImport.sumTwo(1.1,2.1)
function_60_forImport.sumTwo('123','456')

# 函数位置实参的顺序
function_60_forImport.printInfo('张三','男')
function_60_forImport.printInfo('男','张三') #实参顺序错误
function_60_forImport.printInfo(gender = '男',name = '张三') #关键字实参

# 函数形参的默认值
function_60_forImport.printUserInfo('张三')
function_60_forImport.printUserInfo('李丽','女')

# 函数返回值
fullName = function_60_forImport.get_fullName('张','三')
print(fullName)

fullName = function_60_forImport.get_name('张','三')
print(fullName)

fullName = function_60_forImport.get_name('张','三','贵')
print(fullName)

# 函数任意数量的实参-元祖
function_60_forImport.print_peoples('people01')
function_60_forImport.print_peoples('people01', 'people02', 'people03', 'people04', 'people05', 'people06', 'people07', 'people08','people09', 'people10')

function_60_forImport.print_info('女','people01', 'people02', 'people03')
function_60_forImport.print_info('男','people04', 'people05', 'people06', 'people07', 'people08','people09', 'people10')

# 函数任意数量的关键字实参-字典
userInfo =  function_60_forImport.build_info(身高 = '170cm',体重 = '60kg',年龄 = 45)
print(userInfo)

