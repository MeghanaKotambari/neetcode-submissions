import random
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums) - k

        def quickselect(left, right):
            pivot = nums[random.randint(left, right)]
            i, j = left, right

            while i <= j:
                while nums[i] < pivot:
                    i += 1
                while nums[j] > pivot:
                    j -= 1

                if i <= j:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j -= 1

            if target <= j:
                return quickselect(left, j)
            elif target >= i:
                return quickselect(i, right)
            else:
                return nums[target]

        return quickselect(0, len(nums) - 1)