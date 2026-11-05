from typing import List
from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        parent = list(range(len(accounts)))
        rank = [1] * len(accounts)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)

            if rootX == rootY:
                return

            if rank[rootX] < rank[rootY]:
                rootX, rootY = rootY, rootX

            parent[rootY] = rootX
            rank[rootX] += rank[rootY]

        # Map each email to the first account containing it
        email_to_id = {}

        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_id:
                    union(i, email_to_id[email])
                else:
                    email_to_id[email] = i

        # Group emails by their connected component
        components = defaultdict(list)

        for email, account_id in email_to_id.items():
            root = find(account_id)
            components[root].append(email)

        result = []

        for root, emails in components.items():
            result.append([accounts[root][0]] + sorted(emails))

        return result