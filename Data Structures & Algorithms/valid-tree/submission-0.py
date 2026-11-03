from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()

        def dfs(node, parent):
            visited.add(node)

            for neighbor in adj[node]:
                if neighbor == parent:
                    continue

                if neighbor in visited:
                    return False

                if not dfs(neighbor, node):
                    return False

            return True

        return dfs(0, -1) and len(visited) == n