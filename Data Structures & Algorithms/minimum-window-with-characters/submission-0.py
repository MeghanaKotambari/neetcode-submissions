class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        need = {}
        window = {}

        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        have = 0
        need_count = len(need)

        left = 0
        res = [-1, -1]
        res_len = float("inf")

        for right in range(len(s)):
            ch = s[right]
            window[ch] = window.get(ch, 0) + 1

            # This character now satisfies its required frequency
            if ch in need and window[ch] == need[ch]:
                have += 1

            # Window is valid → try to make it smaller
            while have == need_count:
                if right - left + 1 < res_len:
                    res = [left, right]
                    res_len = right - left + 1

                left_ch = s[left]
                window[left_ch] -= 1

                if left_ch in need and window[left_ch] < need[left_ch]:
                    have -= 1

                left += 1

        if res_len == float("inf"):
            return ""

        return s[res[0]:res[1] + 1]