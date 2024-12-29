# coding=utf-8
'''
输入一个二叉树和一个整数，打印出二叉树中节点值的和等于输入整数所有的路径
这道题不是打印路径的话就必须是叶子节点。
'''
from typing import List, Any
from copy import deepcopy
# note : 树路径原题
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def find_trace_only_root_begin(self, nd: TreeNode, find_val: int) -> list[Any]: # 本方法只能获取 root 到节点路径的结果，不能获取非root的结果
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

    def find_trace_all_error(self,nd: TreeNode, find_val: int):
        # 无法实现找到 非根的路径搜索，因为需要记录子节点的两个状态。 这个能通过最大值结合判定当前节点的方法找到，但是遍历路径是找不到的，非常困难抽象成子问题，见124题
        self.trace_holder = []

        def dfs(nd:TreeNode,find_num):
            if not nd: return [],[]
            l_l,l_r = dfs(nd.left,find_num)
            r_l,r_r = dfs(nd.right,find_num)
            tmp_res = [l_l +[nd.val]+l_r,r_l+[nd.val]+r_r]
            for tmp in tmp_res:
                if sum(tmp) == find_val:
                    self.trace_holder.append(deepcopy(tmp +[nd.val]))
            return l_l +[nd.val]+l_r,r_l+[nd.val]+r_r

        dfs(nd,find_val)
        return self.trace_holder



nd = TreeNode(1,TreeNode(-1,None,TreeNode(3,TreeNode(-1))),TreeNode(0,TreeNode(1)))
nd2 = TreeNode(2,TreeNode(0,TreeNode(3),TreeNode(1,TreeNode(1))))

#print(Solution().find_trace_only_root_begin(nd,2))
print(Solution().find_trace_all(nd2,5))