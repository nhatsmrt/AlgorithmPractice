class UnionFind:
    def __init__(self, upper: int):
        self.upper = upper
        self.parents = {}
        self.ranks = {}

    def union(self, num1: int, num2: int):
        ans1, ans2 = self.find(num1), self.find(num2)

        if ans1 != ans2:
            rank1, rank2 = self.ranks.get(ans1, 1), self.ranks.get(ans2, 2)

            if rank1 < rank2:
                self.parents[ans1] = ans2
                self.parents[num1] = ans2
                self.ranks[ans2] = rank1 + rank2
            else:
                self.parents[ans2] = ans1
                self.parents[num2] = ans1
                self.ranks[ans1] = rank1 + rank2

    def find(self, num: int) -> int:
        parent = self.parents.get(num, num)

        if parent == num:
            return num
        else:
            ancestor = self.find(parent)
            self.parents[num] = ancestor

            return ancestor

    def largest_component_size(self, A: List[int]):
        counter = Counter()

        for num in A:
            counter[self.find(num)] += 1

        ret = 0
        for key in counter:
            ret = max(ret, counter[key])

        return ret

class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        # Time Complexity: O(N * log M)
        # Space Complexity: O(N + M)
        uf = UnionFind(max(A))

        for num in A:
            for i in range(2, int(sqrt(num)) + 1):
                if num % i == 0:
                    uf.union(num, i)
                    uf.union(num, num // i)

        return uf.largest_component_size(A)
