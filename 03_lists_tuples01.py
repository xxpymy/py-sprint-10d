def lists_tuples1():
    a = [3,1,3,2,1,5]
    b = []
    for i in a:
        if i not in b:
            b.append(i)
    return b
tuple1 = lists_tuples1()
print(tuple1)