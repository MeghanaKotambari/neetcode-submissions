from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        def backtrack(index):
            if index == len(nums):
                result.append(subset.copy())
                return

            # Include the current number
            subset.append(nums[index])
            backtrack(index + 1)

            # Exclude the current number
            subset.pop()
            backtrack(index + 1)

        backtrack(0)
        return result