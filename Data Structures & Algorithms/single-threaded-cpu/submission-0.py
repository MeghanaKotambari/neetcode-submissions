import heapq
from typing import List

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = sorted(
            (enqueue, process, i)
            for i, (enqueue, process) in enumerate(tasks)
        )

        result = []
        heap = []
        time = 0
        i = 0
        n = len(tasks)

        while len(result) < n:
            # Add all tasks that are available
            while i < n and tasks[i][0] <= time:
                enqueue, process, index = tasks[i]
                heapq.heappush(heap, (process, index))
                i += 1

            if heap:
                process, index = heapq.heappop(heap)
                result.append(index)
                time += process
            else:
                # Jump to the next task's arrival time
                time = tasks[i][0]

        return result