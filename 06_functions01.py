# 23. def add(item, box=[]) 连调 add(1)、add(2)，打印 box；解释为什么第二次是 [1,2]，再改成正确写法
# 24. def total(*nums) 求和；def build(**kw) 合并配置返回 dict
# 25. def min_max(nums) 返回 (最小, 最大)，调用方一行解包
# 26. 对 [{"name":"b","score":80},{"name":"a","score":90},{"name":"c","score":80}] 按 score 降序、score 相同按 name 升序（key 里返回元组）
def add(item, box=None):
    if box is None:
        box = []
    box.append(item)
    print(box)
add(1)
add(2)


