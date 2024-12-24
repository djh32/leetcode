# coding=utf-8
from typing import Optional, List

"""
给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。

路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

输入：root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
输出：3

这道题使用的前缀和，或者两次遍历
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:  # 两次遍历

        def find_node_target_count(nd: TreeNode, need_num: int):  # 第一次递归，找到以当前nd作为根节点，返回所有路径是targetsum的数量
            if not nd:
                return 0
            rtn_val = 0
            if nd.val == need_num:
                rtn_val += 1

            need_num = need_num - nd.val
            rtn_val += find_node_target_count(nd.left, need_num)
            rtn_val += find_node_target_count(nd.right, need_num)
            return rtn_val

        def dfs(root, targetSum):  # 第二次递归，找到以所有节点遍历一遍，作为根的结果求和
            if not root:
                return 0
            val = find_node_target_count(root, targetSum)
            val += dfs(root.left, targetSum)
            val += dfs(root.right, targetSum)
            return val

        return dfs(root, targetSum)


rt = TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4, None, TreeNode(5)))))
#print(Solution().pathSum(rt, 3))


class Solution2:
    def pathSum(self, root: Optional[TreeNode], target_sum: int) -> int:  # 前缀和
        self.pre_holder = {0: 1}
        self.trace_num = 0

        def dfs(root, target_sum,now_pre):
            if not root: return None
            now_pre += root.val
            if (now_pre - target_sum) in self.pre_holder:
                self.trace_num +=self.pre_holder[now_pre - target_sum]

            if now_pre in self.pre_holder:
                self.pre_holder[now_pre] += 1  # 用default dict 也行，不用的话需要判断now_pre_sum 前缀和是不是出现过，以及val=出现册次数。 比如[0,1,1]
            else:
                self.pre_holder.update({now_pre:1})

            dfs(root.left, target_sum,now_pre)
            dfs(root.right, target_sum,now_pre)
            self.pre_holder[now_pre] -= 1 # 这里必须是-1 不能是pop now_pre_sum 因为 [0,1,0] 这种会在第2个0的时候更新0的key，如果pop的时候第一个0不能正确回退。

        dfs(root, target_sum, 0)
        return self.trace_num




#nd = TreeNode(10,TreeNode(5,TreeNode(3),TreeNode(2,None,TreeNode(1))))
nd2 = TreeNode(0,TreeNode(1),TreeNode(0))
nd3 = TreeNode(1)

print(Solution2().pathSum(nd2,1))

