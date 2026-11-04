# 23. def add(item, box=[]) 连调 add(1)、add(2)，打印 box；解释为什么第二次是 [1,2]，再改成正确写法
# 24. def total(*nums) 求和；def build(**kw) 合并配置返回 dict
# 25. def min_max(nums) 返回 (最小, 最大)，调用方一行解包
# 26. 对 [{"name":"b","score":80},{"name":"a","score":90},{"name":"c","score":80}] 按 score 降序、score 相同按 name 升序（key 里返回元组）
def total(*nums):
    total1 = 0
    for num in nums:
        total1 += num
    return total1
print(total(1,2,3,4,5,6))
def build(**kw):
    return kw
print(build(a=1, b=2, c=3))