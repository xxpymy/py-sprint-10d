def abc123():
    try:
        a = int(input())  #引发异常代码
        b = int(input())  #引发异常代码
    except ValueError:
        print("错误：输入无效")
    print("继续")
abc123()