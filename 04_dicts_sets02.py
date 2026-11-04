# 1. "the cat the dog the bird" → 词频字典，必须用 dict.get(w,0)+1，不许用 Counter
# 2. 上题结果按 value 降序取前 3，输出 [('the',3),...]
# 3. 对比 d.get("x",0) 与 d.setdefault("x",0)，打印调用后 d 的样子
# 4. [1,2,3,4] 与 [3,4,5] → 交集、前者独有（set）
s = "the cat the dog the bird"
word_count = {}
# 第1题：统计词频，用 get
# for w in s.split():
#     word_count[w] = word_count.get(w, 0) + 1
#
# # 第2题：按value降序，取前3
# # items()得到 (单词,次数)，排序key取次数，reverse=True降序
# res = sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:3]
# print(res)
for w in s.split():
     word_count[w] = word_count.get(w, 0) + 1
res = sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:3]
print(res)
print(word_count)