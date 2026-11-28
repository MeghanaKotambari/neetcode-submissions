class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        dp = [False] * (n + 1)
        dp[0] = True

        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[j] = dp[j - 2]

        for i in range(1, m + 1):
            curr = [False] * (n + 1)

            for j in range(1, n + 1):
                if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    curr[j] = dp[j - 1]

                elif p[j - 1] == '*':
                    curr[j] = curr[j - 2]

                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        curr[j] |= dp[j]

            dp = curr

        return dp[n]