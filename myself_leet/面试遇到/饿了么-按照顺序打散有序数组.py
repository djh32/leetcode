# //将搜索结果根据品牌进行打散
# //从队列开始到末尾，尽可能多的店铺满足间隔3以内的店铺品牌是不同的。
# //比如“咖啡”搜索结果：B11 B21 B12 B22 B31 B41 B23 打散后： B11 B21 B31 B12 B22 B41 B23
# //比如”星巴克“搜索结果：B11 B12 B13 B14 B15 B16 B17 打散后： B11 B12 B13 B14 B15 B16 B17
# //B1星巴克 B11 星巴克店1； B2 costa B3 瑞幸


# 1,2,1,2,3,4,2
# 题干都没有读明白 很呆
# def sort_find(lst: list):
#     length = len(lst)
#     i = 1
#     res = []
#     while i < length:
#         if lst[i] > lst[i - 1]:
#             res.append(lst[i - 1])
#             i += 1
#         else:
#             tmp, holder = i, lst[i - 1]
#             res.append(lst[i - 1])
#             while tmp < length:
#                 if lst[tmp] > holder:
#                     res.append(lst[tmp])
#                     lst.pop(tmp)
#                 tmp += 1
#             i += 1
#print(sort_find([1, 2, 1, 2, 3, 4, 2]))
from typing import List
from typing import Dict
from collections import deque
from copy import deepcopy
def sort_find_fix(lst: deque[str]):
    d: Dict[str, deque[str]] = {}
    for i in lst:
        type = i[1]
        if type not in d:
            d[type] = deque([i])
        else:
            d[type].append(i)
    print(d)

    tmp_res = deque([x[1] for x in lst])
    print(tmp_res)

    checklistss = deque(deepcopy(lst))
    seen = set()
    res = []
    i = 0
    while checklistss:
        if checklistss[i][1] not in seen:
            add_val = d[checklistss[i][1]].popleft()
            seen.add(checklistss[i][1])
            res.append(add_val)
            checklistss.remove(checklistss[i])
            if len(seen) == 3 or i==len(checklistss):  # 这个or 是为了过 11122 的结果
                seen = set()
                i=0
                continue
        else:
            i +=1
            if i >= len(checklistss):
                seen = set()
                i=0
                continue
    print(res)


#sort_find_fix("B11 B21 B12 B22 B31 B41 B23".replace(" ",',').split(","))
#sort_find_fix("B11 B12 B13 B14 B21 B22".replace(" ",',').split(","))
sort_find_fix("B11 B12 B23 B24 B21 B22 B25".replace(" ",',').split(","))
