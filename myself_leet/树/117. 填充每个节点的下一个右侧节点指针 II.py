# 这个题的深度遍历写法有意思：

# 广度遍历用临时tmp holde当前的状态就好。。
from typing import List


# BFS
# class Solution:
#     def connect(self, root: Node) -> Node:
#         layer_holder: List[Node] = [root]
#         while layer_holder:
#             for i in range(len(layer_holder) - 1):
#                 layer_holder[i].next = layer_holder[i + 1]
#             # pop holder
#             tmp = layer_holder
#             layer_holder = []
#             for nd in tmp:
#                 if nd.left: layer_holder.append(nd.left)
#                 if nd.right: layer_holder.append(nd.right)
#         return root
#
#
# # DFS
# class Solution:
#     def connect(self, root: Node) -> Node:
#         step_current_left = []
#         def dfs_link(nd, deep):
#             if not root:
#                 return None
#             if deep == len(result): # 最左边的node
#                 step_current_left.append(nd)
#             else:
#                 step_current_left[deep].next = nd
#                 step_current_left[deep] = nd
#             dfs_link(nd.left, deep + 1)
#             dfs_link(nd.right, deep + 1)
#
#             return nd
#
#         return dfs_link(root, 0)

class TreeNode(object):
    def __init__(self, val, left=None, right=None, next=None):
        self.val = val
        self.right = right
        self.left = left
        self.next = None


def recur_make(preorder, inorder: List):
    if not inorder:
        return None
    val = preorder.pop(0)
    rt = TreeNode(val)
    idx = inorder.index(val)
    left = inorder[:idx]
    right = inorder[idx + 1:]
    rt.left = recur_make(preorder, left)
    rt.right = recur_make(preorder, right)
    return rt


rt = recur_make([1, 2, 4, 5, 3, 6, 7], [4, 2, 5, 1, 6, 3, 7])
print(rt.val)


def find_next(root:TreeNode):
    cache:dict = {}
    def dfs(deep,root):
        if not root:
            return
        if deep not in cache:
            cache[deep] = [root]
        else:
            cache[deep][-1].next = root
            cache[deep].append(root)
        dfs(deep + 1, root.left)
        dfs(deep + 1, root.right)
        return root

    return dfs(0, root)

rt = find_next(rt)
print(rt.val)


