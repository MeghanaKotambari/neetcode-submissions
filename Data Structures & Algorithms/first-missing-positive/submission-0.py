class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        i = 0

        while i < n:
            # Put nums[i] in its correct position
            correct = nums[i] - 1

            if 1 <= nums[i] <= n and nums[i] != nums[correct]:
                nums[i], nums[correct] = nums[correct], nums[i]
            else:
                i += 1

        # Find the first number in the wrong position
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1