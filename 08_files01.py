# 27. try/except/else/finally 各 print 一句，分别跑“正常”与“除零”两种情况，记录打印顺序
# 28. safe_div(a,b)、get_score(d,name)：除零提示“除数不能为 0”，KeyError 提示“没有这个学生”，禁止裸 except
# 29. read_lines(path)：逐行读、去行尾 \n、跳过空行返回列表；文件不存在返回 [] 并提示“文件不存在”
# 30. log(msg)：追加写 app.log，每行 2026-11-04 13:58 | msg（datetime.now().strftime）
def test():
    try:

        x = 10 / 2    # 正常情况
        #x = 10 / 0
        print("try")     # 除零报错情况
    except ZeroDivisionError:
        print("except")
    else:
        print("else")
    finally:
        print("finally")

test()