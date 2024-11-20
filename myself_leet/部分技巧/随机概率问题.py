# coding=utf-8
"""
随机的(0,1)生成0-1000的随机数据
"""
import collections
import random
# def rand():
#     return random.randint(0, 1)
#
#
# def gettmp():
#     tmp = ''
#     # 没次结果都是独立的，连续10次可以视为0-1024内均匀随机
#     for _ in range(10):
#         tmp += str(rand())
#     return tmp
#
#
# res = [9999] * 1000000
# for i in range(1000000):
#     dd = int(gettmp(), base=2)
#     if dd < 1001:
#         res[i] = dd
# # 看下结果统计
# aa = collections.Counter(res)
# # 去除掉9999（被拒绝掉的大于1000的部分）
# aa.pop(9999)
# # 出现最多的次数
# print(max(aa.values()))  # 1077
# # 出现最少的次数
# print(min(aa.values()))  # 894
# # 元素个数
# print(len(aa))  # 1001  [0-1000]

"""
rand5 表示rand7
"""


def rand7():
    r5a = random.randint(1, 5)
    r5b = random.randint(1, 5)
    r5_rand = (r5a - 1) * 5 + r5b  # [1,25]
    if r5_rand <= 21:
        return r5_rand % 7 +1
    else:
        r5a = random.randint(1, 5)
        r5b = random.randint(1, 5)
        r5_rand = (r5a - 1) * 5 + r5b  # [1,25]
        if r5_rand <= 21:
            return r5_rand % 7 + 1
        else:
            r5a = random.randint(1, 5)
            r5b = random.randint(1, 5)
            r5_rand = (r5a - 1) * 5 + r5b  # [1,25]
            if r5_rand <= 21:
                return r5_rand % 7 + 1
            else:
                return -1

"""
class Solution extends SolBase {
    public int rand10() {
        while(true) {
            int a = rand7();
            int b = rand7();
            int num = (a-1)*7 + b; // rand 49
            if(num <= 40) return num % 10 + 1; // 拒绝采样
            
            a = num - 40; // rand 9
            b = rand7();
            num = (a-1)*7 + b; // rand 63
            if(num <= 60) return num % 10 + 1;
            
            a = num - 60; // rand 3
            b = rand7();
            num = (a-1)*7 + b; // rand 21
            if(num <= 20) return num % 10 + 1;
        }
    }
}

作者：kkbill
链接：https://leetcode.cn/problems/implement-rand10-using-rand7/solutions/167850/cong-zui-ji-chu-de-jiang-qi-ru-he-zuo-dao-jun-yun-/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""

d = collections.defaultdict()
for _ in range(1000000):
    r = rand7()
    if r not in d:
        d[r] = 1
    else:
        d[r]+=1
print(d)

# d = collections.defaultdict()
# for _ in range(10000000):
#     r = random.randint(1, 5)
#     if r not in d:
#         d[r] = 1
#     else:
#         d[r]+=1
# print(d)