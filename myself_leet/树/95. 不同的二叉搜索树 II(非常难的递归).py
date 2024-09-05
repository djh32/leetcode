# Definition for a binary tree node.
from typing import Optional, List

"""
给你一个整数 n ，请你生成并返回所有由 n 个节点组成且节点值从 1 到 n 互不相同的不同 二叉搜索树 。可以按 任意顺序 返回答案。

示例 1
输入：n = 3
输出：[[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]

示例 2：
输入：n = 1
输出：[[1]]
 
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    res = 0

    def generateTrees(self, n: int):
        hold_list = list(range(1, n + 1))

        def dfs(left_idx, right_idx):
            layer_node = []
            if left_idx == right_idx:
                layer_node.append(TreeNode(left_idx))
                return layer_node
            if left_idx > right_idx:
                return [None]

            for i in range(left_idx, right_idx + 1):
                left_nodes = dfs(left_idx, i - 1)
                right_nodes = dfs(i + 1, right_idx)
                for lnd in left_nodes:
                    for rnd in right_nodes:
                        rt = TreeNode(val=i)
                        rt.left = lnd
                        rt.right = rnd
                        layer_node.append(rt)
            return layer_node

        res = dfs(1, n)
        return res


x = Solution().generateTrees(5)
print(len(x))
