from functools import lru_cache
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)

        max_len = max(map(len, words))

        @lru_cache(None)
        def dfs(start: int) -> List[str]:
            if start == len(s):
                return [""]

            result = []

            for end in range(start + 1, min(start + max_len, len(s)) + 1):
                word = s[start:end]

                if word in words:
                    for suffix in dfs(end):
                        if suffix:
                            result.append(word + " " + suffix)
                        else:
                            result.append(word)

            return result

        return dfs(0)