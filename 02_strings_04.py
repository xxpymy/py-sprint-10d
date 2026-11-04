def huiwen(s):
    s1 = s.upper()
    s2 = s1[::-1]
    if s1 == s2:
        print(f"{s}是回文")
    else:
        print(f"{s}不是回文")
huiwen(input())