class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)

        while left <= right:
            max_sum = left + (right - left) // 2

            subarrays = 1
            current_sum = 0

            for num in nums:
                if current_sum + num > max_sum:
                    subarrays += 1
                    current_sum = 0

                current_sum += num

            if subarrays <= k:
                right = max_sum - 1
            else:
                left = max_sum + 1

        return left