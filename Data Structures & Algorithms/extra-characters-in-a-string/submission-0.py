from typing import List

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        words = set(dictionary)
        n = len(s)

        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            # Treat s[i] as an extra character
            dp[i] = 1 + dp[i + 1]

            # Try every dictionary word starting at i
            for j in range(i + 1, n + 1):
                if s[i:j] in words:
                    dp[i] = min(dp[i], dp[j])

        return dp[0]