from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        if len(temperatures)>0:
            stack = [(0,temperatures[0])] # [(idx,temper)]
        else:
            return [0]
        for idx in range(1, len(temperatures)):
            temp = temperatures[idx]
            while len(stack)>0 and temp > stack[-1][1]:
                top_idx,top_temp = stack.pop(-1)
                res[top_idx] = idx - top_idx
            stack.append((idx,temp))

        for (idx,temp) in stack:
            res[idx] = 0
        return res

print(Solution().dailyTemperatures([73, 73]))
