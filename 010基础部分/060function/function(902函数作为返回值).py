# 函数作为返回值计算几何特性
def aeraRectangle(length,width): #矩形面积
        return length*width

def volumeCuboid(length,width,height): #长方体体积
        return length*width*height

def calculateGeometry(calculateFor):
        if calculateFor == 'aerajuxing':
                return aeraRectangle #函数作为返回值
        if calculateFor == 'volumejuxing':
                return volumeCuboid #函数作为返回值

calGeometry = calculateGeometry('aerajuxing')
print(str(calGeometry(4,5)))
calGeometry = calculateGeometry('volumejuxing')
print(calGeometry(4,5,6))