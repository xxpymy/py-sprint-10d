#["name","age"] + ["Tom",18] → 字典（zip）
a = ["name","age"]
b = ["Tom",18]
c = dict(zip(a,b))
print(c)