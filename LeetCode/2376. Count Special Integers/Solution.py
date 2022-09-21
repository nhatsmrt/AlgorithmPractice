def count(digit, used, is_smaller, is_started, upper_bound_digits, solutions):
    if digit == len(upper_bound_digits):
        if is_started:
            return 1
        else:
            return 0

    if (digit, used, is_smaller, is_started) in solutions:
        return solutions[(digit, used, is_smaller, is_started)]

    upper_bound = 9 if is_smaller else upper_bound_digits[digit]
    ret = 0

    for cand in range(upper_bound + 1):
        flag = 1 << cand
        if not is_started or not (used & flag):
            new_is_started = is_started or cand != 0
            new_used = used | flag if new_is_started else used

            ret += count(
                digit + 1,
                new_used,
                is_smaller or cand < upper_bound_digits[digit],
                new_is_started,
                upper_bound_digits,
                solutions
            )

    solutions[(digit, used, is_smaller, is_started)] = ret
    return ret


class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        # Time and Space Complexity: O(W)
        # where W is the number of digits of n
        # note that bitmask is at most 2^10 - 1 = 1023

        ret = count(0, 0, False, False, list(map(int, str(n))), {})
        return ret
