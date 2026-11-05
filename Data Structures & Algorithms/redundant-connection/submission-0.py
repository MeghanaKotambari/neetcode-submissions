from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges) + 1))
        rank = [1] * (len(edges) + 1)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)

            if rootX == rootY:
                return False

            # Union by rank
            if rank[rootX] < rank[rootY]:
                rootX, rootY = rootY, rootX

            parent[rootY] = rootX
            rank[rootX] += rank[rootY]

            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]