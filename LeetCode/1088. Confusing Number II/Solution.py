class Solution:
    def confusingNumberII(self, N: int) -> int:
        # Time Complexity: O(W * 5^W)
        # Space Complexity: O(W)

        digs = []
        self.N = N
        while N > 0:
            digs.append(N % 10)
            N //= 10

        self.digs = list(reversed(digs))
        return self.build([], False)

    def to_num(self, digs):
        ret = 0

        for dig in digs:
            ret = ret * 10 + dig

        return ret

    def build(self, partial_sol, less_than):
        if len(partial_sol) == len(self.digs):
            first_non_zero = 0
            while first_non_zero < len(partial_sol) and not partial_sol[first_non_zero]:
                first_non_zero += 1

            if first_non_zero == len(partial_sol):
                return 0


            value = self.to_num(partial_sol)
            is_confusing = self.to_num(map(lambda d: 15 - d if d in [6, 9] else d, reversed(partial_sol[first_non_zero:]))) != value
            ret = 1 if value <= self.N and is_confusing else 0
        else:
            ret = 0
            for cand in [0, 1, 6, 8, 9]:
                if less_than or cand <= self.digs[len(partial_sol)]:
                    # early pruning of invalid branches
                    partial_sol.append(cand)
                    ret += self.build(partial_sol, less_than or cand < self.digs[len(partial_sol) - 1])
                    partial_sol.pop()

        return ret
