from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        # Build Trie
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word

        rows, cols = len(board), len(board[0])
        result = []

        def dfs(r, c, node):
            char = board[r][c]

            if char not in node.children:
                return

            child = node.children[char]

            # Found a complete word
            if child.word is not None:
                result.append(child.word)
                child.word = None  # Avoid duplicates

            # Mark cell as visited
            board[r][c] = "#"

            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc

                if (0 <= nr < rows and 0 <= nc < cols
                        and board[nr][nc] != "#"):
                    dfs(nr, nc, child)

            # Restore the cell
            board[r][c] = char

            # Prune Trie branches with no remaining words
            if not child.children and child.word is None:
                del node.children[char]

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return result