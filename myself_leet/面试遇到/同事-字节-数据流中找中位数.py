# coding=utf-8
from typing import List
import heapq
"""
中位数是有序整数列表中的中间值。如果列表的大小是偶数，则没有中间值，中位数是两个中间值的平均值。

例如 arr = [2,3,4] 的中位数是 3 。
例如 arr = [2,3] 的中位数是 (2 + 3) / 2 = 2.5 。
实现 MedianFinder 类:

MedianFinder() 初始化 MedianFinder 对象。

void addNum(int num) 将数据流中的整数 num 添加到数据结构中。

double findMedian() 返回到目前为止所有元素的中位数。与实际答案相差 10-5 以内的答案将被接受。

示例 1：

输入
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
输出
[null, null, null, 1.5, null, 2.0]

解释
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // 返回 1.5 ((1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0


"""

import heapq


class MedianFinder:

    def __init__(self):
        self.bg_first_hp = []
        self.sm_first_hp =[]

    def addNum(self, num: int) -> None:
        if len(self.bg_first_hp) == len(self.sm_first_hp):
            heapq.heappush(self.bg_first_hp,-num)
            min = heapq.heappop(self.bg_first_hp)
            heapq.heappush(self.sm_first_hp,-min)
        else:
            heapq.heappush(self.sm_first_hp,num)
            max_hp = heapq.heappop(self.sm_first_hp)
            heapq.heappush(self.bg_first_hp,-max_hp)

    def findMedian(self) -> float:
        if len(self.bg_first_hp) == len(self.sm_first_hp):
            heapq.heapify(self.sm_first_hp)
            heapq.heapify(self.bg_first_hp)
            res = (self.sm_first_hp[0] -self.bg_first_hp[0])/2.0
        else:
            heapq.heapify(self.sm_first_hp)
            res = self.sm_first_hp[0]
        return res

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()



mf = MedianFinder()
mf.addNum(1)
mf.addNum(3)
mf.addNum(5)
mf.addNum(7)
mf.addNum(9)
mf.addNum(11)
mf.addNum(13)
mf.addNum(15)
mf.findMedian()
mf.addNum(17)
mf.addNum(19)

pass



