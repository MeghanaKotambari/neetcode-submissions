class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c):
            if dp[r][c]:
                return dp[r][c]

            dp[r][c] = 1

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] > matrix[r][c]:
                    dp[r][c] = max(dp[r][c], 1 + dfs(nr, nc))

            return dp[r][c]

        return max(dfs(i, j) for i in range(m) for j in range(n))