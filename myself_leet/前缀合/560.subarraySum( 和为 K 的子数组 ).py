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

class Solution2:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 前缀和
        cache = {0:1}
        sum = 0
        res = 0
        for n in nums:
            sum += n
            need = sum - k
            if need in cache: # 注意这里需要先根据need找到当前sum的结果和k的差距是不是存在于记录中，
                # 前缀和的差，代表中间连续数据的和(不包含第一个)
                # 所以当前sum-k如果存在于前缀和之中，那么连续自数组肯定存在 +1就行，结果就是[sum]。
                res += cache[need]
            if sum in cache:
                cache[sum] +=1
            else:
                cache.update({sum: 1})

        return res
# 比如[-2, 1, 2, 3, -1, -2, 5] 的前缀和结果是[0,-2,-1,1,4,3,1,6]
# 这里多一个sum=0，这个是必要的。
# 那么第5个sum=4 - 第一个sum=-2的结果是6 代表 从1到5个求和是6，如果k=6那么就是自数组。
print(Solution().subarraySum(nums=[-2, 1, 2, 3, -1, -2, 5], k=5))
print(Solution2().subarraySum(nums=[1,2,-1,-2,0,0], k=0))
