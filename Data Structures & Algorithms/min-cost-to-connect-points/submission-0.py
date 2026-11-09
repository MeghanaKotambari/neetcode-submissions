from typing import List
import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        visited = set()
        min_heap = [(0, 0)]
        total_cost = 0

        while len(visited) < n:
            cost, i = heapq.heappop(min_heap)

            if i in visited:
                continue

            visited.add(i)
            total_cost += cost

            x1, y1 = points[i]

            for j in range(n):
                if j not in visited:
                    x2, y2 = points[j]
                    distance = abs(x1 - x2) + abs(y1 - y2)
                    heapq.heappush(min_heap, (distance, j))

        return total_cost