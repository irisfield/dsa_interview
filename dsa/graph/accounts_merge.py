class UnionFind:
    def __init__(self, n):
        # Each element is its own parent initially
        self.parent = list(range(n))
        # Each set starts with size 1
        self.size = [1] * n

    # Find with Path Compression
    def find(self, x):
        # If x is not its own parent, continue recursively
        if self.parent[x] != x:
            # Path compression: flatten the structure
            self.parent[x] = self.find(self.parent[x])
        # Return the root (representative of the set)
        return self.parent[x]

    # Union by Size
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        # Only union if they are in different sets
        if rootX != rootY:
            # Union by size: Attach the smaller tree under the larger one
            if self.size[rootX] < self.size[rootY]:
                # Swap to make rootX always the larger set
                rootX, rootY = rootY, rootX
            # Attach rootY's tree under rootX's tree
            self.parent[rootY] = rootX
            # Update size of the new root's tree
            self.size[rootX] += self.size[rootY]

class Solution:
    """721. Accounts Merge"""

    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        uf = UnionFind(len(accounts))
        account_owner = {}  # email : index of account

        for index, account in enumerate(accounts):
            for email in account[1:]:
                if email in account_owner:
                    uf.union(index, account_owner[email])
                else:
                    account_owner[email] = index

        email_group = {}
        for email, index in account_owner.items():
            parent = uf.find(index)
            if parent not in email_group:
                email_group[parent] = []
            email_group[parent].append(email)

        res = []
        for parent, emails in email_group.items():
            name = accounts[parent][0]
            res.append([name] + sorted(emails))

        """
        The time complexity is O(A * α(N)), where A is the total number
        of emails across all accounts, N is the number of accounts, andα
        is the inverse Ackermann function, which grows extremely slowly
        (better than O(log n)). This complexity arises from performing
        union and find operations for each email and account.

        The space complexity is O(A), where A is the total number of
        emails. This accounts for the storage in the Union-Find data
        structure and the mappings for email ownership and email
        grouping.
        """
        return res
