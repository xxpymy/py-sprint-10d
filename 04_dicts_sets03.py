# 1. "the cat the dog the bird" → 词频字典，必须用 dict.get(w,0)+1，不许用 Counter
# 2. 上题结果按 value 降序取前 3，输出 [('the',3),...]
# 3. 对比 d.get("x",0) 与 d.setdefault("x",0)，打印调用后 d 的样子
# 4. [1,2,3,4] 与 [3,4,5] → 交集、前者独有（set）
def dicts():
    d1 = {}
    d2 = {}
    c = d1.get("x",0)
    e = d2.setdefault("x",0)
    print(d1)
    print(d2)
dicts()
