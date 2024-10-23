#coding=utf-8
from typing import List
import math

def recur_find(nums:int):
    l,r = 0,nums
    m = l + (r - l)/2.
    while abs(m*m - nums) > 0.0001:
        m = l + (r - l) / 2.
        if m*m <nums: #right
            l = m
        else:
            r=m
        print(m,r)
    return m


print(recur_find(3))









