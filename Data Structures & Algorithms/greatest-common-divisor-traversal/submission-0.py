class Solution:
    def canTraverseAllPairs(self, nums: list[int]) -> bool:
        n = len(nums)

        if n == 1:
            return True

        if 1 in nums:
            return False

        max_num = max(nums)

        spf = list(range(max_num + 1))

        for i in range(2, int(max_num ** 0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, max_num + 1, i):
                    if spf[j] == j:
                        spf[j] = i

        parent = list(range(n))
        size = [1] * n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra = find(a)
            rb = find(b)

            if ra == rb:
                return

            if size[ra] < size[rb]:
                ra, rb = rb, ra

            parent[rb] = ra
            size[ra] += size[rb]

        prime_owner = {}

        for i, num in enumerate(nums):
            while num > 1:
                p = spf[num]

                if p in prime_owner:
                    union(i, prime_owner[p])
                else:
                    prime_owner[p] = i

                while num % p == 0:
                    num //= p

        root = find(0)

        for i in range(1, n):
            if find(i) != root:
                return False

        return True