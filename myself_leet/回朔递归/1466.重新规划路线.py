from typing import List
from copy import deepcopy

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        cache = set([0])
        result= 0
        def recur(cache: set, left_list: List[List[int]]):
            nonlocal result
            if not left_list:
                return 0
            new_list = deepcopy(left_list)
            for idx in range(len(left_list)):
                from_node, to_node = left_list[idx]
                if to_node in cache:
                    cache.add(from_node)
                    new_list.pop(new_list.index([from_node, to_node]))
                    continue
                if from_node in cache:
                    result +=1
                    cache.add(to_node)
                    new_list.pop(new_list.index([from_node, to_node]))
                    continue
            return recur(cache,new_list)

        recur(cache,connections)
        return result







class Solution2:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        def dfs(a, parent):
            # return sum(c + dfs(b, a) for b, c in g[a] if b != parent)
            res = 0
            for b, c in g[a]:
                if b != parent:
                    res += dfs(b, a) + c
            return res

        g = [[] for _ in range(n)]
        for a, b in connections:
            g[a].append((b, 1))
            g[b].append((a, 0))

        return dfs(0, -1)

print(Solution().minReorder(5,[[0,4],[1,2],[3,2],[3,4]]))





