from typing import List
'''
给出一个无重叠的 ，按照区间起始端点排序的区间列表。

在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

 

示例 1：

输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
输出：[[1,5],[6,9]]
示例 2：

输入：intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
输出：[[1,2],[3,10],[12,16]]
解释：这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。
 

注意：输入类型已在 2019 年 4 月 15 日更改。请重置为默认代码定义以获取新的方法签名。
'''


# https://leetcode.cn/problems/insert-interval/solutions/472435/shou-hua-tu-jie-57-cha-ru-qu-jian-fen-cheng-3ge-ji/
class Solution:

    def intersected(self,a, b):
        if a[0] > b[1] or a[1] < b[0]: # 当前i的最小值比new的还要大， 或者 当前i的大值比new的要小，都是不能插入的点，否命题都是能插入的点
            # 其实这里只用a[0] > b[1] 就行了
            return False
        return True

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i=0
        res = []
        # 前
        while i <len(intervals) and intervals[i][1]<newInterval[0]: # 大值比new的要小，直接插入
            res.append(intervals[i])
            i +=1
        # 中
        while i < len(intervals) and self.intersected(intervals[i], newInterval): # 直接点，不考虑那么多

        #while i <len(intervals) and intervals[i][0]<=newInterval[1]:
            # 隐含条件：当前i右端值比new的左值要大或者等于，已经有重合了需要开始更新newInterval
            # 这个时候只需要判断当前i的左端 和融合new的右端比较， 如果i左端小于等于new右端则有重合需要融合，否则退出融合阶段
            newInterval[0] = min(intervals[i][0],newInterval[0])
            newInterval[1] = max(intervals[i][1],newInterval[1])
            i +=1
        res.append(newInterval)
        #后
        while i < len(intervals) and intervals[i][0] > newInterval[1]:
            res.append(intervals[i])
            i += 1
        return res


class Solution_me:
    '''
    自己写的，感觉能写出来结果根本不用考虑这么复杂。
    '''
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i =0
        res = []
        while i<=len(intervals)-1:
            tmp_res = intervals[i]
            if intervals[i][1] >= newInterval[0]: # newInterval[0]重合在i下标对应的
                new_left = intervals[i][0]
                j = i+1
                new_right = newInterval[1]
                while j<=len(intervals)-1:
                    if intervals[j][1]>=newInterval[1]:
                        new_right = intervals[j][1]
                        j += 1
                        i = j-1
                        break
                    j +=1
                    i = j-1
                tmp_res = [new_left,new_right]
                res.append(tmp_res)
                res.extend(intervals[j:])
                return res
            res.append(tmp_res)
            i +=1
        return res
print(Solution_me().insert(intervals=[[1,3],[6,9]],newInterval=[2,5]))

