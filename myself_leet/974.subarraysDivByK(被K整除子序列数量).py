# 题目地址(974. 和可被 K 整除的子数组)
# 利用了同余定理：P[j]modk==P[i−1]modk，就可以保证上面的等式成立 P[i]=nums[0]+nums[1]+…+nums[i]
# 如果P[j]modk==P[i−1]modk 则能确定：  (P[j]−P[i−1]) mod k==0
from typing import  List
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum,ans = 0,0
        mod_info = {0:1}
        for num in nums:
            prefix_sum += num
            m = prefix_sum % k
            seen_time = mod_info.get(m,0)
            ans += seen_time
            mod_info[m] = seen_time+1
        return ans

print(Solution().subarraysDivByK([4,5,0,-2,-3,1],k=5))