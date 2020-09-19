def num_dig(num: int) -> int:
    ret = 0

    while num > 0:
        ret += 1
        num //= 10

    return ret

def to_num(digs: List[int]) -> int:
    ret = 0

    for dig in digs:
        ret = ret * 10 + dig

    return ret


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits = list(map(lambda dig: dig + 1, range(9)))

        low_num_dig = num_dig(low)
        high_num_dig = num_dig(high)

        ret = []

        for length in range(low_num_dig, high_num_dig + 1):
            for i in range(0, len(digits) - length + 1):
                window = to_num(digits[i:i + length])

                if low <= window and window <= high:
                    ret.append(window)

        return ret
