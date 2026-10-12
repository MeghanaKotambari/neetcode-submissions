import random
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(point):
            return point[0] ** 2 + point[1] ** 2

        left, right = 0, len(points) - 1

        while left <= right:
            pivot = distance(points[random.randint(left, right)])
            i, j = left, right

            while i <= j:
                while i <= j and distance(points[i]) < pivot:
                    i += 1
                while i <= j and distance(points[j]) > pivot:
                    j -= 1

                if i <= j:
                    points[i], points[j] = points[j], points[i]
                    i += 1
                    j -= 1

            if k <= j + 1:
                right = j
            elif k >= i:
                left = i
            else:
                break

        return points[:k]