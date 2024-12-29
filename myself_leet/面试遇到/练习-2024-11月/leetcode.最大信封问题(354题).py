from typing import List
from copy import deepcopy

'''
354. 俄罗斯套娃信封问题
给你一个二维整数数组 envelopes ，其中 envelopes[i] = [wi, hi] ，表示第 i 个信封的宽度和高度。

当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。

请计算 最多能有多少个 信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。
注意：不允许旋转信封。
 
示例 1：
输入：envelopes = [[5,4],[6,4],[6,7],[2,3]]
输出：3
解释：最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。

示例 2：
输入：envelopes = [[1,1],[1,1],[1,1]]
输出：1

'''
# note 原题

class Solution:
    def find_insert(self, nums, val):
        l, r = 0, len(nums)
        while l < r:
            mid = l + (r - l) // 2
            if val < nums[mid]:
                r = mid
            elif val > nums[mid]:
                l = mid + 1
            else:
                return mid
        return r

    def LSF_nums(self, nums):
        sorted_holder = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > sorted_holder[-1]:
                sorted_holder.append(nums[i])
            else:
                insert_idx = self.find_insert(sorted_holder, nums[i])
                sorted_holder[insert_idx] = nums[i]
        return len(sorted_holder)

    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        st_envelopes = sorted(envelopes, key=lambda x: (x[0], -x[1]))  # 必须0升序 1降序，避免idx1升序错位。
        idx_1 = [x[1] for x in st_envelopes]
        # 找到idx1 里面最长上升子序列的个数就行
        # print(st_envelopes,idx_1)
        max_lift_seq_ken = self.LSF_nums(idx_1)
        # print("result",max_lift_seq_ken)
        return max_lift_seq_ken


Solution().maxEnvelopes([[5, 4], [6, 8], [6, 12], [1, 4], [7, 17], [2, 3]])
