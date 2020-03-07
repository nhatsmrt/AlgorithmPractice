class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Time Complexity: O(log n)
        # Space Complexity: O(1)

        if (dividend == -2147483648 and divisor == -1):
            return 2147483647

        if divisor < 0 and dividend < 0:
            return self.divide(-dividend, -divisor)

        if dividend > 0 and divisor < 0:
            return -self.divide(dividend, -divisor)

        if dividend < 0 and divisor > 0:
            return -self.divide(-dividend, divisor)

        if dividend < divisor:
            return 0

        factor = divisor
        power = 1

        while factor <= dividend:
            power <<= 1
            factor <<= 1

        factor >>= 1
        power >>= 1

        ret = 0
        while factor > 0:
            if dividend >= factor:
                ret += power
                dividend -= factor
            factor >>= 1
            power >>= 1


        return ret
