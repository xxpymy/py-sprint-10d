def liebao1():
    a = "a,b;c d|e"
    b = []
    for c in a:
        if c.isalpha():
            b.append(c)
    print(b)
liebao1()