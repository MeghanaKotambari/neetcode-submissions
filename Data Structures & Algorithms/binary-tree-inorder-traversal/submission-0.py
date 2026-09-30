class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        curr = root

        while curr or stack:
            # Go as far left as possible
            while curr:
                stack.append(curr)
                curr = curr.left

            # Visit node
            curr = stack.pop()
            result.append(curr.val)

            # Move to right subtree
            curr = curr.right

        return result