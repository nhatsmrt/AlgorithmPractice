from functools import partial


class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        # Time Complexity: N 2^N
        # Space Complexity: 2^N

        if N == 1:
            return [i for i in range(10)]

        self.dp = {}

        ret = []
        for i in range(1, 10):
            sols = list(map(
                lambda suf: i * 10 ** (N - 1) + suf,
                self.build_sol(i, N - 1, K)
            ))
            ret.extend(sols)

        return ret


    def build_sol(self, last: int, remaining: int, diff: int) -> List[int]:
        if (last, remaining) in self.dp:
            return self.dp[(last, remaining)]

        next_digs = list(set(filter(lambda dig: dig >= 0 and dig <= 9, [last + diff, last - diff])))

        if remaining == 1:
            ret = next_digs
        else:
            ret = []
            for next_dig in next_digs:
                sols = list(map(
                    lambda suf: next_dig * 10 ** (remaining - 1) + suf,
                    self.build_sol(next_dig, remaining - 1, diff)
                ))
                ret.extend(sols)

        self.dp[(last, remaining)] = ret
        return ret
