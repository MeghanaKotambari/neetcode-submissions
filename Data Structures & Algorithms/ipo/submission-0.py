import heapq
from typing import List

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = sorted(zip(capital, profits))
        max_heap = []
        i = 0
        n = len(projects)

        for _ in range(k):
            # Add all projects we can currently afford
            while i < n and projects[i][0] <= w:
                heapq.heappush(max_heap, -projects[i][1])
                i += 1

            # No affordable projects remain
            if not max_heap:
                break

            # Choose the most profitable available project
            w += -heapq.heappop(max_heap)

        return w