from typing import List

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)

        if total % k != 0:
            return False

        target = total // k
        n = len(nums)

        if max(nums) > target:
            return False

        dp = [-1] * (1 << n)
        dp[0] = 0

        for mask in range(1 << n):
            if dp[mask] == -1:
                continue

            for i in range(n):
                if mask & (1 << i):
                    continue

                new_sum = dp[mask] + nums[i]

                if new_sum <= target:
                    new_mask = mask | (1 << i)
                    dp[new_mask] = new_sum % target

        return dp[(1 << n) - 1] == 0