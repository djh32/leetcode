# 这个题的深度遍历写法有意思：

# 广度遍历用临时tmp holde当前的状态就好。。

# BFS
class Solution:
    def connect(self, root: Node) -> Node:
        layer_holder: List[Node] = [root]
        while layer_holder:
            for i in range(len(layer_holder) - 1):
                layer_holder[i].next = layer_holder[i + 1]
            # pop holder
            tmp = layer_holder
            layer_holder = []
            for nd in tmp:
                if nd.left: layer_holder.append(nd.left)
                if nd.right: layer_holder.append(nd.right)
        return root


# DFS
class Solution:
    def connect(self, root: Node) -> Node:
        step_current_left = []
        def dfs_link(nd, deep):
            if not root:
                return None
            if deep == len(result): # 最左边的node
                step_current_left.append(nd)
            else:
                step_current_left[deep].next = nd
                step_current_left[deep] = nd
            dfs_link(nd.left, deep + 1)
            dfs_link(nd.right, deep + 1)

            return nd

        return dfs_link(root, 0)
