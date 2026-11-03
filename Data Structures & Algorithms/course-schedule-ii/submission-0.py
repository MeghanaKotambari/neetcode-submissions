from collections import deque
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        # Build graph
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegree[course] += 1

        # Add courses with no prerequisites
        queue = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        result = []

        # BFS (Kahn's Algorithm)
        while queue:
            course = queue.popleft()
            result.append(course)

            for neighbor in adj[course]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # Check for cycle
        return result if len(result) == numCourses else []