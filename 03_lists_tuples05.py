#("张三",25,"测试") 一行解包成三个变量；再交换 a,b
def lists_tuples05():

    a,b,c = ("张三",25,"测试")
    a,b = b,a
    print(a,b,c)
lists_tuples05()