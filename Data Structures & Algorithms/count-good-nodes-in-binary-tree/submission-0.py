class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, max_value):
            if not node:
                return 0

            count = 0

            if node.val >= max_value:
                count = 1

            max_value = max(max_value, node.val)

            count += dfs(node.left, max_value)
            count += dfs(node.right, max_value)

            return count

        return dfs(root, root.val)