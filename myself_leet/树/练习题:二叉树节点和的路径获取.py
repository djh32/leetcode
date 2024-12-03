# coding=utf-8
'''
输入一个二叉树和一个整数，打印出二叉树中节点值的和等于输入整数所有的路径
'''
from typing import List, Any
from copy import deepcopy

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def find_trace(self, nd: TreeNode, find_val: int) -> list[Any]:
        self.result = []

        def dfs(nd: TreeNode, tmp_trace):
            if not nd: return None
            now_trace = deepcopy(tmp_trace) # 注意透传的参数，每个节点需要缓存目前的状态一个，方便之后回溯
            now_trace.append(nd.val)
            now_num = sum(now_trace)
            if now_num == find_val:
                self.result.append(deepcopy(now_trace))
            dfs(nd.left, now_trace)
            dfs(nd.right, now_trace)
            return nd

        dfs(nd, [])
        return self.result
    # def find_trace_error(self, nd: TreeNode, find_val: int) -> list[Any]:
    #     self.result = []
    #
    #     def dfs(nd: TreeNode, holder_num, tmp_trace):
    #         if not nd: return None
    #         tmp_trace.append(nd.val)
    #         now_num = sum(tmp_trace)
    #         if now_num == find_val:
    #             self.result.append(tmp_trace)
    #         dfs(nd.left, now_num, tmp_trace)
    #         dfs(nd.right, now_num, tmp_trace)
    #     dfs(nd,0,[])
    #     return self.result

nd = TreeNode(1,TreeNode(-1,None,TreeNode(3,TreeNode(-1))),TreeNode(0,TreeNode(1)))

print(Solution().find_trace(nd,2))