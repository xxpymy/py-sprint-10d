# 20. 判断闰年，用 2000/1900/2024/2023 测四个值，期望 True/False/True/False
# 21. 打印 1–100 中能被 3 整除且不能被 5 整除的数，空格分隔一行输出
# 22. while True + input()，输入 quit 退出并报“共输入 N 次”；空输入 continue 不计数
def loop1():
    count = 0
    while True:
        s = input("请输入内容：")
        if s == "quit":
            print(f"共输入 {count} 次")
            break
        elif s == "":
            print("空字符，重新输入")
            continue
        else:
            print("输入错误，重新输入")
            count += 1
            continue
        # 空输入，不计数，直接下一轮循环


loop1()