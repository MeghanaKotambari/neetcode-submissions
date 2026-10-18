from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()
        current = []

        def backtrack(start, remaining):
            if remaining == 0:
                result.append(current.copy())
                return

            for i in range(start, len(nums)):
                if nums[i] > remaining:
                    break

                current.append(nums[i])
                backtrack(i, remaining - nums[i])  # Reuse allowed
                current.pop()

        backtrack(0, target)
        return result