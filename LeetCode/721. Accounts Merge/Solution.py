class UnionFind:
    def __init__(self, emails):
        self.emails = emails
        self.info = [""] * len(emails)
        self.rank = [1] * len(emails)
        self.parents = [i for i in range(len(emails))]

        for email, (name, index) in emails.items():
            self.info[index] = name, email

    def union(self, acc1: str, acc2: str):
        node1, node2 = self.emails[acc1][1], self.emails[acc2][1]

        if self.find(node1) != self.find(node2):
            par1 = self.find(node1)
            par2 = self.find(node2)

            # union by rank:
            if self.rank[par1] < self.rank[par2]:
                self.parents[node1] = par2
                self.parents[par1] = par2

                self.rank[par2] += self.rank[par1]
            else:
                self.parents[node2] = par1
                self.parents[par2] = par1

                self.rank[par1] += self.rank[par2]

    def find(self, node: int) -> int:
        if self.parents[node] == node:
            return node

        # path compression
        self.parents[node] = self.find(self.parents[node])
        return self.parents[node]

    def get_final_accounts(self) -> List[List[str]]:
        final_accs = {}

        for node in range(len(self.parents)):
            self.find(node)

        for node in range(len(self.parents)):
            par = self.parents[node]

            if par not in final_accs:
                final_accs[par] = self.info[par][0], [self.info[par][1]]

            if par != node:
                final_accs[par][1].append(self.info[node][1])

        ret = []
        for node in final_accs:
            ret.append([final_accs[node][0]] + sorted(final_accs[node][1]))

        return ret



class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emails = {}

        for account in accounts:
            name = account[0]

            for i in range(1, len(account)):
                if account[i] not in emails:
                    emails[account[i]] = (name, len(emails))

        uf = UnionFind(emails)

        for account in accounts:
            for i in range(1, len(account) - 1):
                node1 = account[i]
                node2 = account[i + 1]

                uf.union(node1, node2)

        return uf.get_final_accounts()
                
