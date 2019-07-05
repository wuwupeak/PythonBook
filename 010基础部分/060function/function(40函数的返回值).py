# 函数返回值
def get_fullName(lastname,firstname):
        return (lastname+firstname)

fullName = get_fullName('张','三')
print(fullName)

def get_name(lastname,firstname,middleName = ''):#使用默认值增强灵活性
        return(lastname + middleName + firstname)

fullName = get_name('张', '三')
print(fullName)
fullName = get_name('张', '三', '贵')
print(fullName)

# 函数可以返回多个值
def get_name(lastname,firstname,middleName = ''): # 使用默认值增强灵活性
        return(lastname, middleName + firstname)
lastname, firstname = get_name('张', '三', '贵')
print("输入的姓是：" + lastname + "，输入的名是：" + firstname + "。")