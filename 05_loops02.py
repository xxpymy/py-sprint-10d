# 20. 判断闰年，用 2000/1900/2024/2023 测四个值，期望 True/False/True/False
# 21. 打印 1–100 中能被 3 整除且不能被 5 整除的数，空格分隔一行输出
# 22. while True + input()，输入 quit 退出并报“共输入 N 次”；空输入 continue 不计数
def loop1():
    a = []
    for x in range(1,101):
        if x%3 == 0 and x%5 != 0:
            a.append(str(x))
    print(" ".join(a))
loop1()