# https://leetcode.cn/problems/subarray-sum-equals-k/solutions/1447027/python3-by-wu-qiong-sheng-gao-de-qia-non-w6jw/
#

from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total_sum, ans = 0, 0
        cache_dict = {}  # cache_dict 存储的是key为到当前的totalsum，value是出现次数。
        for num in nums:
            total_sum += num
            if total_sum == k:
                ans += 1
            if total_sum - k in cache_dict:
                # 最重要的一步，如果total_sum - k 可以在表中找到。
                # 说明total_sum - k：之前的sum下的value可以作为延伸，value出现次数中每一个结果都可以和当前的num组成k，
                # 所以ans += cache_dict.get(total_sum - k)
                ans += cache_dict.get(total_sum - k)
                print(num,total_sum - k,cache_dict.get(total_sum - k),ans,cache_dict)
            if total_sum in cache_dict:
                cache_dict[total_sum] += 1
            else:
                cache_dict[total_sum] = 1
        return ans


print(Solution().subarraySum(nums=[-2, 1, 2, 3, -1, -2, 5], k=5))
