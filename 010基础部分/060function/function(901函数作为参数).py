#一个没有拆分的代码范例
def calculateGeometry(calName,para1,para2 = 0,para3 = 0):
        if(calName == 'aeraRectangle'):
                return para1*para2
        if(calName == 'volumeCuboid'):
                return para1*para2*para3
        if(calName == 'aeraCircle'):
                return math.pi * para1**2
        if(calName == 'volumeSphere'):
                return 4*math.pi * para1**3/3


# # 函数作为参数计算几何特性
# import math #引入数学计算包
# def aeraRectangle(length,width): #矩形面积
#         return length * width
# # aeraRectangleResult = aeraRectangle(3,4)
# # aeraOutput =  str(aeraRectangleResult)
# # print(aeraOutput)

# def volumeCuboid(length,width,height): #长方体体积
#         return length * width * height

# # def aeraCircle(radius): #圆形面积
# #         return math.pi * radius**2

# def volumeSphere(radius): #球形体积
#         return 4*math.pi * radius**3/3

# def aeraCircle(radius): #圆形面积
#         return math.pi * radius**2












# 函数作为参数计算几何特性
import math #引入数学计算包
def aeraRectangle(length,width,parameterC = 0): #矩形面积
        return length * width

def volumeCuboid(length,width,height): #长方体体积
        return length * width * height

def aeraCircle(radius,parameterB=0,parameterC = 0): #圆形面积
        return math.pi * radius**2

def volumeSphere(radius,parameterB=0,parameterC = 0): #球形体积
        return 4*math.pi * radius**3/3

def calculateGeometry(calFunc,parameterA,parameterB = 0,parameterC = 0): #使用函数作为参数，并使用了默认参数值
        return calFunc(parameterA,parameterB,parameterC)

print(calculateGeometry(aeraRectangle,4,5))
print(calculateGeometry(volumeCuboid,1,2,3))
print(calculateGeometry(aeraCircle,0.5))
print(calculateGeometry(volumeSphere,1))