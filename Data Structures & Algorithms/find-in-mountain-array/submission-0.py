class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()

        # 1. Find peak
        left = 0
        right = n - 1

        while left < right:
            mid = left + (right - left) // 2

            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                left = mid + 1
            else:
                right = mid

        peak = left

        # 2. Binary search increasing part
        left = 0
        right = peak

        while left <= right:
            mid = left + (right - left) // 2
            value = mountainArr.get(mid)

            if value == target:
                return mid
            elif value < target:
                left = mid + 1
            else:
                right = mid - 1

        # 3. Binary search decreasing part
        left = peak + 1
        right = n - 1

        while left <= right:
            mid = left + (right - left) // 2
            value = mountainArr.get(mid)

            if value == target:
                return mid
            elif value > target:
                left = mid + 1
            else:
                right = mid - 1

        return -1