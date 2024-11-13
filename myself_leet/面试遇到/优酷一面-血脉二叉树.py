"""
《二又树的“一脉相承“问题》
 针对二叉树中的节点，定义如下概念：
血缘关系：对2个节点A和B，如果A是B的祖先或A是B的子孙，那么，A和B是有“血缘关系”的。
一脉相承：给定一个节点List，如果List中的任意2个不同的节点都是有“血缘关系”的，那么，这个节点List就是“一脉相承”的。
// 要求实现一个函数，判断一个节点List是不是“一脉相承”的：
// 函数的输入：一个二叉树根节点：root；一个二叉树节点List:nodeList
1/ 函数的输出：boolean。true代表nodeList是“一脉相承”的，false代表nodeList不是“一脉相承”的。
// 编程语言不限。

下面case里面
其中，[A、C、H］是一脉相承的，［B、G]是一脉相承的，[A、F、I]是一脉相承的，[A、F、H]不是一脉相承的。
"""
from typing import List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preFindMark(self, root):
        self.mark_dict = {}
        self.all_time = 0

        def dfs(root: TreeNode):
            if not root: return
            # 进入time
            self.all_time += 1  # 应该先+1 再记录， 如果先记录再+1的话 有节点的进入值 和 上个遍历节点的出值相同。
            tmp_in_time = self.all_time
            dfs(root.left)
            dfs(root.right)
            self.all_time += 1
            tmp_out_time = self.all_time
            self.mark_dict[root.val] = [tmp_in_time, tmp_out_time]

        dfs(root)

    def findAncestor(self, nd_list: List[List[int]]):
        dq = deque(nd_list)
        while len(dq) > 1:
            nd1 = dq.popleft()
            nd2 = dq.popleft()
            if (nd1[0] > nd2[0] and nd1[1] < nd2[1]) or (nd1[0] < nd2[0] and nd1[1] > nd2[1]):
                merge_one = nd1 if nd1[0] > nd2[0] else nd2
                dq.append(merge_one)
            else:
                return False
        return True


root = TreeNode('A', TreeNode('B', TreeNode('D', TreeNode('G'))),
                TreeNode('C', TreeNode('E', None, TreeNode('H')), TreeNode('F', None, TreeNode('I'))))
a = Solution()
a.preFindMark(root)
print(a.mark_dict)
give_dict = ['A', 'G', 'D']
tmp_list = [a.mark_dict[k] for k in give_dict]
print(a.findAncestor(tmp_list))
