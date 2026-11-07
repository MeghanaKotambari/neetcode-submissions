from typing import List
from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        word_len = len(beginWord)
        patterns = defaultdict(list)

        for word in wordList:
            for i in range(word_len):
                pattern = word[:i] + "*" + word[i + 1:]
                patterns[pattern].append(word)

        queue = deque([(beginWord, 1)])
        visited = {beginWord}

        while queue:
            word, steps = queue.popleft()

            if word == endWord:
                return steps

            for i in range(word_len):
                pattern = word[:i] + "*" + word[i + 1:]

                for neighbor in patterns[pattern]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, steps + 1))

                # Avoid processing the same pattern repeatedly
                patterns[pattern] = []

        return 0