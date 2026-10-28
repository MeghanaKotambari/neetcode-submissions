from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        rank = {char: i for i, char in enumerate(order)}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]

            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    if rank[c1] > rank[c2]:
                        return False
                    break
            else:
                # If w2 is a prefix of w1, the order is invalid
                if len(w1) > len(w2):
                    return False

        return True