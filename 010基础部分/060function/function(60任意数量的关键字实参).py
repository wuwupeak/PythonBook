# 任意数量的关键字实参-字典
def build_info(**user):
        userInfo = {}
        for key,value in user.items():
                userInfo[key] = value
        return userInfo
userInfo =  build_info(身高 = '170cm',体重 = '60kg',年龄 = 45)
print(userInfo)