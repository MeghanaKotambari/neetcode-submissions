class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        result = []

        def dfs(node):
            if not node:
                result.append("N")
                return

            result.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(result)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = iter(data.split(","))

        def dfs():
            val = next(values)

            if val == "N":
                return None

            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()