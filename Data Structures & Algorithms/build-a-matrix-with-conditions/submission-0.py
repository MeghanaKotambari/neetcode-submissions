from collections import deque

class Solution:
    def buildMatrix(self, k: int, rowConditions: list[list[int]],
                    colConditions: list[list[int]]) -> list[list[int]]:

        def topo_sort(conditions):
            adj = [[] for _ in range(k + 1)]
            indegree = [0] * (k + 1)

            for u, v in conditions:
                adj[u].append(v)
                indegree[v] += 1

            q = deque()

            for i in range(1, k + 1):
                if indegree[i] == 0:
                    q.append(i)

            order = []

            while q:
                node = q.popleft()
                order.append(node)

                for nei in adj[node]:
                    indegree[nei] -= 1

                    if indegree[nei] == 0:
                        q.append(nei)

            if len(order) != k:
                return []

            return order

        row_order = topo_sort(rowConditions)
        col_order = topo_sort(colConditions)

        if not row_order or not col_order:
            return []

        row_pos = [0] * (k + 1)
        col_pos = [0] * (k + 1)

        for i, num in enumerate(row_order):
            row_pos[num] = i

        for i, num in enumerate(col_order):
            col_pos[num] = i

        ans = [[0] * k for _ in range(k)]

        for num in range(1, k + 1):
            ans[row_pos[num]][col_pos[num]] = num

        return ans