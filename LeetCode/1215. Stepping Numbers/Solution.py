def num_to_digits(num):
    return list(map(int, str(num)))

class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        # Time and Space Complexity: O(2^{log_10(high)})

        high_digits = num_to_digits(high)
        low_digits = num_to_digits(low)
        low_digits = [0] * (len(high_digits) - len(low_digits)) + low_digits

        ret = []
        self.build(0, low_digits, high_digits, False, False, False, 0, 0, ret)
        return ret



    def build(self, partial_sol, low_bound, high_bound, bigger_than_low, smaller_than_high, is_start, num_digit, last_digit, ret):
        if num_digit == len(low_bound):
            ret.append(partial_sol)
        else:
            start = 0 if bigger_than_low else low_bound[num_digit]
            end = 9 if smaller_than_high else high_bound[num_digit]

            cands = range(10) if not is_start else (last_digit - 1, last_digit+ 1)

            for cand in cands:
                if start <= cand <= end:
                    self.build(
                        partial_sol * 10 + cand,
                        low_bound, high_bound,
                        bigger_than_low or cand > low_bound[num_digit],
                        smaller_than_high or cand < high_bound[num_digit],
                        is_start or cand != 0,
                        num_digit + 1,
                        cand,
                        ret
                    )
