from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        current = []

        def backtrack(start):
            result.append(current.copy())

            for i in range(start, len(nums)):
                # Skip duplicate values at the same recursion level
                if i > start and nums[i] == nums[i - 1]:
                    continue

                current.append(nums[i])
                backtrack(i + 1)
                current.pop()

        backtrack(0)
        return result