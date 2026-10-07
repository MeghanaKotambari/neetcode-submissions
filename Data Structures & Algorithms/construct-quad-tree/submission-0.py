class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def dfs(r, c, size):
            # Check if all values in this region are the same
            first = grid[r][c]
            same = True

            for i in range(r, r + size):
                for j in range(c, c + size):
                    if grid[i][j] != first:
                        same = False
                        break
                if not same:
                    break

            # If all values are the same, create a leaf
            if same:
                return Node(first == 1, True)

            half = size // 2

            return Node(
                False,
                False,
                dfs(r, c, half),                  # topLeft
                dfs(r, c + half, half),            # topRight
                dfs(r + half, c, half),            # bottomLeft
                dfs(r + half, c + half, half)      # bottomRight
            )

        return dfs(0, 0, len(grid))