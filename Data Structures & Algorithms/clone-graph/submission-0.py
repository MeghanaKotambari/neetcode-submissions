class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        if not node:
            return None

        clones = {}

        def dfs(curr):
            if curr in clones:
                return clones[curr]

            clone = Node(curr.val)
            clones[curr] = clone

            for neighbor in curr.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        return dfs(node)