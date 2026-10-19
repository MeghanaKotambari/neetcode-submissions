from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        path = []

        def backtrack(start: int) -> None:
            if len(path) == k:
                result.append(path.copy())
                return

            for num in range(start, n - (k - len(path)) + 2):
                path.append(num)
                backtrack(num + 1)
                path.pop()

        backtrack(1)
        return result