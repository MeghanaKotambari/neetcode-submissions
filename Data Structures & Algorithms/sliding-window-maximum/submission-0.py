from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        window = deque()

        for right in range(len(nums)):
            # Remove elements outside the window
            while window and window[0] < right - k + 1:
                window.popleft()

            # Remove smaller elements from the back
            while window and nums[window[-1]] <= nums[right]:
                window.pop()

            # Add current index
            window.append(right)

            # Window has reached size k
            if right >= k - 1:
                result.append(nums[window[0]])

        return result