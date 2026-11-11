class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n, edges):
        edges = [(u, v, w, i)
                 for i, (u, v, w) in enumerate(edges)]

        edges.sort(key=lambda x: x[2])

        class DSU:
            def __init__(self, n):
                self.parent = list(range(n))
                self.rank = [0] * n

            def find(self, x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]

            def union(self, x, y):
                px = self.find(x)
                py = self.find(y)

                if px == py:
                    return False

                if self.rank[px] < self.rank[py]:
                    px, py = py, px

                self.parent[py] = px

                if self.rank[px] == self.rank[py]:
                    self.rank[px] += 1

                return True

        def kruskal(skip=-1, force=-1):
            dsu = DSU(n)
            weight = 0
            count = 0

            if force != -1:
                u, v, w, _ = edges[force]
                dsu.union(u, v)
                weight += w
                count += 1

            for i, (u, v, w, idx) in enumerate(edges):
                if i == skip or i == force:
                    continue

                if dsu.union(u, v):
                    weight += w
                    count += 1

            if count != n - 1:
                return float('inf')

            return weight

        mst_weight = kruskal()

        critical = []
        pseudo = []

        for i, edge in enumerate(edges):
            original_idx = edge[3]

            if kruskal(skip=i) > mst_weight:
                critical.append(original_idx)

            elif kruskal(force=i) == mst_weight:
                pseudo.append(original_idx)

        return [critical, pseudo]