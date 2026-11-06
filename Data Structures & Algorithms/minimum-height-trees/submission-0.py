from typing import List
from collections import defaultdict, deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        graph = defaultdict(list)
        degree = [0] * n

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1

        queue = deque(i for i in range(n) if degree[i] == 1)
        remaining = n

        while remaining > 2:
            size = len(queue)
            remaining -= size

            for _ in range(size):
                node = queue.popleft()

                for neighbor in graph[node]:
                    degree[neighbor] -= 1

                    if degree[neighbor] == 1:
                        queue.append(neighbor)

        return list(queue)