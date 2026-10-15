from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)

        if max(count.values()) > (len(s) + 1) // 2:
            return ""

        heap = [(-freq, char) for char, freq in count.items()]
        heapq.heapify(heap)

        result = []
        prev_freq = 0
        prev_char = ""

        while heap:
            freq, char = heapq.heappop(heap)
            result.append(char)

            if prev_freq < 0:
                heapq.heappush(heap, (prev_freq, prev_char))

            freq += 1
            prev_freq, prev_char = freq, char

        return "".join(result)