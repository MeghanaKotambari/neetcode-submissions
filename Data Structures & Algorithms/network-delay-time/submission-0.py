from typing import List
from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))

        dist = [float('inf')] * (n + 1)
        dist[k] = 0

        min_heap = [(0, k)]

        while min_heap:
            time, node = heapq.heappop(min_heap)

            if time > dist[node]:
                continue

            for neighbor, weight in graph[node]:
                new_time = time + weight

                if new_time < dist[neighbor]:
                    dist[neighbor] = new_time
                    heapq.heappush(min_heap, (new_time, neighbor))

        result = max(dist[1:])

        return result if result != float('inf') else -1