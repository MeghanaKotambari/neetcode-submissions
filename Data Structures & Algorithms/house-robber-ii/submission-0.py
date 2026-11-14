class Solution:
    def rob(self, nums: List[int]) -> int:

        def robRange(arr):
            prev2 = prev1 = 0

            for num in arr:
                prev2, prev1 = prev1, max(prev1, prev2 + num)

            return prev1

        n = len(nums)

        if n == 1:
            return nums[0]

        return max(robRange(nums[:-1]), robRange(nums[1:]))