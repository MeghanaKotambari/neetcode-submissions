class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        stack = []
        current = root

        while True:
            # Go as far left as possible
            while current:
                stack.append(current)
                current = current.left

            # Visit node
            current = stack.pop()
            k -= 1

            if k == 0:
                return current.val

            # Move to right subtree
            current = current.right