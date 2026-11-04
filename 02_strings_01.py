def hellostr():
    s = "hello world hello"
    num = s.count("hello")
    print(num)
hellostr()


def hellostr2(s,str1):
    if not str1 or len(str1) > len(s):
        return 0
    num = 0
    m = len(str1)
    for i in range(len(s)-len(str1)+1):
        if s[i:i+m] == str1:
            num += 1
    print(num)
hellostr2("hello word hello","hello")

