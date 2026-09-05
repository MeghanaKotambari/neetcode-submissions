class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        max_freq = 0
        result = 0

        for right, char in enumerate(s):
            count[char] = count.get(char, 0) + 1
            max_freq = max(max_freq, count[char])

            # Characters that need to be replaced
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)

        return result