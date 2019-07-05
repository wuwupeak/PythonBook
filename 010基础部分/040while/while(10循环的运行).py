# while 循环
show = "\n请输入文本消息，程序将重复显示"
show += "\n输入'exit'将退出程序"
message = ""
while message != 'exit':
        message = input(show)
        if message != 'exit':
                print(message)

#while循环使用状态控制跳出
show = "\n请输入文本消息，程序将重复显示"
show += "\n输入'exit'将退出程序"
active = True
while active:
        message = input(show)
        if message == 'exit':
                active = False #使用while循环内的状态位进行控制
        else:
                print(message)