from typing import List
from copy import deepcopy

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


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isback(strings) -> bool:
            if len(strings) <= 1: return True
            l, r = 0, len(strings) - 1
            while r > l:
                if strings[l] != strings[r]:
                    return False
                r -= 1
                l += 1
            return True

        def backtracking(strings, tempresult: List):
            if len(strings) == 0:
                res.append(deepcopy(tempresult))
                return
            for idx in range(len(strings)):
                leftstrings = strings[:idx + 1]
                rightstrings = strings[idx + 1:]
                if not isback(leftstrings):
                    continue
                tempresult.append(leftstrings)
                backtracking(rightstrings, tempresult)
                tempresult.pop(-1)

            return res

        temp = []
        backtracking(s, temp)
        return res


def play2(s: str) -> List[List[str]]:
    res = []

    def back_str(ss: str):
        if len(ss) < 2: return True
        l, r = 0, len(ss) - 1
        while l < r and ss[l] == ss[r]:
            l += 1
            r -= 1

        if l >= r:
            return True
        else:
            return False
    def recur(test_str: List[str], left_str: str):
        if left_str == "":
            res.append(deepcopy(test_str))

        layer_temper = test_str
        for i in range(len(left_str)):
            left = left_str[:i + 1]
            layer_temper.append(left)
            right = left_str[i + 1:]
            if back_str(left):
                recur(layer_temper, right)
            layer_temper.pop(-1)

        return res
    recur([],s)
    return res

#print(play2("a"))
print(play2("aaab"))
