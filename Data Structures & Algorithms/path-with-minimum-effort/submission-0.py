from typing import List
import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])

        efforts = [[float('inf')] * cols for _ in range(rows)]
        efforts[0][0] = 0

        min_heap = [(0, 0, 0)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while min_heap:
            effort, r, c = heapq.heappop(min_heap)

            if r == rows - 1 and c == cols - 1:
                return effort

            if effort > efforts[r][c]:
                continue

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    diff = abs(heights[r][c] - heights[nr][nc])
                    new_effort = max(effort, diff)

                    if new_effort < efforts[nr][nc]:
                        efforts[nr][nc] = new_effort
                        heapq.heappush(min_heap, (new_effort, nr, nc))

        return 0