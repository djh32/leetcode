# https://leetcode.cn/problems/subarray-sum-equals-k/solutions/1447027/python3-by-wu-qiong-sheng-gao-de-qia-non-w6jw/
#

from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total_sum, ans = 0, 0
        cache_dict = {}
        for num in nums:
            total_sum += num
            if total_sum == k:
                ans +=1
            if total_sum - k in cache_dict:# 最重要的一步，如果total_sum - k 可以在表中找到，说明total_sum"曾经"命中过"k" 那么k的次数对应value
                ans += cache_dict.get(total_sum - k)
            if total_sum in cache_dict:
                cache_dict[total_sum] += 1
            else:
                cache_dict[total_sum] =1
        return ans


print(Solution().subarraySum(nums=[1, 2, 3, -1, -2], k=5))
