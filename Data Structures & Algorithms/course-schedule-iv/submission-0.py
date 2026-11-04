from typing import List

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        # Reachability matrix
        reach = [[False] * numCourses for _ in range(numCourses)]

        # Direct prerequisites
        for u, v in prerequisites:
            reach[u][v] = True

        # Floyd-Warshall: find indirect prerequisites
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    reach[i][j] = reach[i][j] or (
                        reach[i][k] and reach[k][j]
                    )

        # Answer queries
        return [reach[u][v] for u, v in queries]