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


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numToChar = {2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'], 5: ['j', 'k', 'l'], 6: ['m', 'n', 'o'],
                     7:['p','q','r','s'],8:['t','u','v'],9:['w','x','y','z']
                     }
        res = []
        def backtracking(digit,res_part:List):
            if digit=='':
                res.append("".join(res_part))
                return
            now = digit[0]
            val = numToChar[int(now)]
            leave = digit[1:]
            for c in val:
                res_part.append(c)
                backtracking(leave,res_part)
                res_part.pop(-1)
        if digits == "":return res
        backtracking(digits,[])
        return res

print(Solution().letterCombinations("23"))
