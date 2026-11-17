
        
from bisect import bisect_left
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []

        for num in nums:
            pos = bisect_left(dp, num)

            if pos == len(dp):
                dp.append(num)
            else:
                dp[pos] = num

        return len(dp)
