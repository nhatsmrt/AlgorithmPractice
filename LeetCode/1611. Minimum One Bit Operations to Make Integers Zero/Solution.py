def to_digits(num):
    ret = []

    while num:
        ret.append(num % 2)
        num //= 2

    return ret[::-1]

def to_pow_2(digits, i):
    if i == len(digits) - 1 and digits[-1] == 1:
        return 0

    if i == len(digits) - 1 and digits[-1] == 0:
        return 1

    if digits[i] == 1:
        return to_zeros(digits, i + 1)

    return to_pow_2(digits, i + 1) + 1 + 2 ** (len(digits) - 1 - i) - 1

def to_zeros(digits, i):
    if i == len(digits) - 1 and digits[-1] == 1:
        return 1

    if i == len(digits) - 1 and digits[-1] == 0:
        return 0

    if digits[i] == 0:
        return to_zeros(digits, i + 1)

    return to_pow_2(digits, i + 1)  + 1 + 2 ** (len(digits) - 1 - i) - 1


class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        # Time and Space Complexity: O(log_2(n))
        # For each digit i, only to_pow_2(i) or to_zeros(i) is called

        if n <= 1:
            return n

        return to_zeros(to_digits(n), 0)
