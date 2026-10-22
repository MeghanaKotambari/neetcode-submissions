from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        current = []

        def isPalindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def backtrack(start):
            if start == len(s):
                result.append(current.copy())
                return

            for end in range(start, len(s)):
                if isPalindrome(start, end):
                    current.append(s[start:end + 1])
                    backtrack(end + 1)
                    current.pop()

        backtrack(0)
        return result