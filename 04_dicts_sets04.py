# 1. "the cat the dog the bird" → 词频字典，必须用 dict.get(w,0)+1，不许用 Counter
# 2. 上题结果按 value 降序取前 3，输出 [('the',3),...]
# 3. 对比 d.get("x",0) 与 d.setdefault("x",0)，打印调用后 d 的样子
# 4. [1,2,3,4] 与 [3,4,5] → 交集、前者独有（set）
def dicts():
    a = [1, 2, 3, 4]
    b = [3, 4, 5]
    s1 = set(a)
    s2 = set(b)
#设置成集合
    jiaoji = s1 & s2  # 交集
    only_a = s1 - s2  # a独有（差集）

    print("交集：", jiaoji)
    print("前者独有：", only_a)
dicts()
def dicts1():
    a = [1, 2, 3, 4, 5, 7]
    b = [3, 4, 5,1]
    s1 = set(a)
    s2 = set(b)
    jiaoji1 = s1 & s2
    onlya = s1 - s2
    print(jiaoji1)
    print(onlya)
dicts1()