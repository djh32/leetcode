# coding=utf-8
from typing import List
import math
import math


def recur_find(nums: int):  # 只有1以上正确
    l, r = 0, nums+1
    m = l + (r - l) / 2.
    while abs(m * m - nums) > 0.0001:
        m = l + (r - l) / 2.
        if m * m < nums:  # right
            l = m
        else:
            r = m
        print(m, r)
    return m


def recur_find2(nums: int):  # 小数正确
    l, r = 0, nums+1 # 这里必须有+1 否则0.4这种小于1的数据找不到右边界 面试的时候可以装一装
    m = l + (r - l) / 2.
    while abs(m * m - nums) > 0.00000001:
        m = l + (r - l) / 2.
        if m*m < nums:
            l = m
        else:
            r = m
    return l



print(recur_find(0.4))

#print(pow(1.5,2))
#print(recur_find2(0.23))