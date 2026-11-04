def abccba(s):
    a = ""
    b = len(s)
    for i in range(b):
         a = a + s[b-1-i]
         i +=1
    print(a)
abccba("abcdef")
def abccba1(s):
    b = s[::-1]
    print(b)
abccba1("abcdef")