from typing import List

'''
存在一个由 n 个节点组成的无向连通图，图中的节点按从 0 到 n - 1 编号。

给你一个数组 graph 表示这个图。其中，graph[i] 是一个列表，由所有与节点 i 直接相连的节点组成。

返回能够访问所有节点的最短路径的长度。你可以在任一节点开始和停止，也可以多次重访节点，并且可以重用边。

 
示例 1：


输入：graph = [[1,2,3],[0],[0],[0]]
输出：4
解释：一种可能的路径为 [1,0,2,0,3]
'''

from collections import  deque
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)

        # 1.初始化队列及标记数组，存入起点
        q = deque((i, 1 << i, 0) for i in range(n))  # 三个属性分别为 idx, mask, dist；存入起点，起始距离0，标记
        vis = {(i, 1 << i) for i in range(n)}  # 节点编号及当前状态

        # 开始搜索
        while q:
            u, mask, dist = q.popleft()  # 弹出队头元素
            if mask == (1 << n) - 1:  # 找到答案，返回结果
                return dist
            # 扩展
            for x in graph[u]:
                nextmask = mask | (1 << x)
                if (x, nextmask) not in vis:
                    q.append((x, nextmask, dist + 1))
                    vis.add((x, nextmask))

        return 0

print(Solution().shortestPathLength(graph = [[1,2,3],[0],[0],[0]]))
