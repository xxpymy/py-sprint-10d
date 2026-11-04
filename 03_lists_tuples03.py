def lists_tuples03():
    list1 = ["apple", "fig", "banana", "kiwi"]
    # 先复制一份，不破坏原始数据
    arr = list1.copy()
    list2 = []

    while arr:
        # 假设第一个是最小的
        min_idx = 0
        for j in range(1, len(arr)):
            # 比较规则：先比长度，长度相等再比字符串
            if len(arr[j]) < len(arr[min_idx]) or (len(arr[j]) == len(arr[min_idx]) and arr[j] < arr[min_idx]):
                min_idx = j
        # 取出最小的放进结果
        list2.append(arr.pop(min_idx))
    print(list2)


lists_tuples03()

def lists_tuples0301():
    list1 = ["apple", "fig", "banana", "kiwi"]
    list2 = list1.copy()
    list3 = []
    while list2:
        min_list2 = 0
        for i in range(1, len(list2)):
            if len(list2[i]) > len(list2[min_list2]) or len(list2[i]) == len(list2[min_list2]) and list2[i] > list2[min_list2]:
                min_list2 = i
        list3.append(list2.pop(min_list2))
    print(list3)
lists_tuples0301()