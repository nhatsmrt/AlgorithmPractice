def to_digit(num: int) -> List[int]:
    ret = []

    while num > 0:
        ret.append(num % 10)
        num //= 10

    return list(reversed(ret))

def to_num(digs: List[int]) -> int:
    ret = 0

    for dig in digs:
        ret = ret * 10 + dig

    return ret


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        low_digs = to_digit(low)
        high_digs = to_digit(high)

        ret = []
        if len(low_digs) == len(high_digs):
            self.build(low_digs, high_digs, len(low_digs), 0, False, False, [], ret)

            return ret

        smallest = [1] + [0] * (len(high_digs) - 1)
        biggest = [9] * len(high_digs)

        self.build(low_digs, biggest, len(low_digs), 0, False, False, [], ret)
        for i in range(len(low_digs) + 1, len(high_digs)):
            self.build(smallest, biggest, i, 0, False, False, [], ret)

        self.build(smallest, high_digs, len(high_digs), 0, False, False, [], ret)

        return ret

    def build(
        self,
        lower_bound: List[int],
        upper_bound: List[int],
        num_digs: int,
        pos: int,
        is_smaller: bool,
        is_larger: bool,
        partial_sol: List[int],
        ret: List[int]
    ):
        if len(partial_sol) == num_digs:
            ret.append(to_num(partial_sol))
        elif not pos:
            low = lower_bound[0]
            high = upper_bound[0]

            for cand in range(low, high + 1):
                partial_sol.append(cand)
                self.build(
                    lower_bound,
                    upper_bound,
                    num_digs,
                    pos + 1,
                    is_smaller or cand < upper_bound[pos],
                    is_larger or cand > lower_bound[pos],
                    partial_sol,
                    ret
                )
                partial_sol.pop()
        else:
            if is_larger:
                low = 0
            else:
                low = lower_bound[pos]

            if is_smaller:
                high = 9
            else:
                high = upper_bound[pos]

            next_dig = partial_sol[-1] + 1

            if low <= next_dig and next_dig <= high:
                partial_sol.append(next_dig)
                self.build(
                    lower_bound,
                    upper_bound,
                    num_digs,
                    pos + 1,
                    is_smaller or next_dig < upper_bound[pos],
                    is_larger or next_dig > lower_bound[pos],
                    partial_sol,
                    ret
                )
                partial_sol.pop()
        
