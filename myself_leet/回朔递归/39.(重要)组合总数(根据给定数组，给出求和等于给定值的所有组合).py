from typing import List

'''
void backtracking(参数) {
    if (终止条件) {
        存放结果;
        return;
    }
    for (选择：本层集合中元素（树中节点孩子的数量就是集合的大小）) {
        处理节点;
        backtracking(路径，选择列表); // 递归
        回溯，撤销处理结果
    }
}

作者：代码随想录
链接：https://leetcode.cn/problems/n-queens/solutions/2566744/dai-ma-sui-xiang-lu-leetcode51nhuang-hou-hcat/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

from copy import deepcopy

# https://leetcode.cn/problems/combination-sum/solutions/14697/hui-su-suan-fa-jian-zhi-python-dai-ma-java-dai-m-2/
# https://www.bilibili.com/video/BV1mG4y1A7Gu/?spm_id_from=333.788&vd_source=f9ab6f2d4e24cf3a1c910bcc71ac84c9
'''
排列问题，讲究顺序（即 [2, 2, 3] 与 [2, 3, 2] 视为不同列表时），需要记录哪些数字已经使用过，此时用 used 数组；
组合问题，不讲究顺序（即 [2, 2, 3] 与 [2, 3, 2] 视为相同列表时），需要按照某种顺序搜索，此时使用 begin 变量。

作者：liweiwei1419
链接：https://leetcode.cn/problems/combination-sum/solutions/14697/hui-su-suan-fa-jian-zhi-python-dai-ma-java-dai-m-2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
class Solution:

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def backtracking(candidates, target, path: List[int], index):
            if sum(path) == target:
                result.append(deepcopy(path))
            if sum(path) >= target:
                return True

            if index < len(candidates):
                # 不选择
                backtracking(candidates, target, path, index + 1)
                # 选择：
                path.append(candidates[index])
                backtracking(candidates, target, path, index)
                path.pop(-1)

        backtracking(candidates, target, [], 0)
        return result

class Solution2:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        # 关键点在于如果是[2,4,7]组合， 那么当前路径选2之后下一步依旧能选择[2,4,7]，但是当前选择4的路径，后面就不能选择4之前的了
        # 因为2的枚举会和它重复！
        def backtracking(candidates, target, path: List[int], begin):
            if sum(path)== target:
                result.append(path.copy())
                return
            if sum(path) >target: return

            for i in range(begin,len(candidates)):
                path.append(candidates[i])
                backtracking(candidates,target,path,i)
                path.pop(-1)

        backtracking(candidates, target, [], 0)
        return result

class Solution3:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        st_cand = sorted(candidates)
        result = []
        def backtracking(st_cand, target, path: List[int], begin):
            if sum(path)== target:
                result.append(path.copy())
                return

            for i in range(begin,len(st_cand)):
                path.append(st_cand[i])
                if sum(path) > target:# 最优方法还是排序以后剪枝，不排序需要多次枚举不能提前剪枝进行结束会降低效率。\
                    path.pop(-1)
                    break
                backtracking(st_cand,target,path,i)
                path.pop(-1)


        backtracking(st_cand, target, [], 0)
        return result
print(Solution2().combinationSum([4, 3, 7, 1,2], 7))
print(Solution3().combinationSum([4, 3, 7], 17))
