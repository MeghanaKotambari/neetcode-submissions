from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(index):
            if index == len(nums):
                result.append(nums.copy())
                return

            for i in range(index, len(nums)):
                nums[index], nums[i] = nums[i], nums[index]

                backtrack(index + 1)

                nums[index], nums[i] = nums[i], nums[index]  # Undo swap

        backtrack(0)
        return result