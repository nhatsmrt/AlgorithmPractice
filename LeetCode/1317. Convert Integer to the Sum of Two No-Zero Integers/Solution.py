def to_num(digs):
    ret = 0
    power = 1

    for dig in digs:
        ret += dig * power
        power *= 10

    return ret


class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        # Time and Space Complexity: O(W) = O(log N)

        num1, num2 = [], []
        carry = 0
        digits = list(reversed(list(map(int, str(n)))))

        for i, dig in enumerate(digits):
            tot = dig - carry
            carry = 0

            if tot <= 1 and i < len(digits) - 1:
                tot += 10
                carry = 1

            num1.append(tot // 2)
            num2.append(tot - num1[-1])

        return [to_num(num1), to_num(num2)]
