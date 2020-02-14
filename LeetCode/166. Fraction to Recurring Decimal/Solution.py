class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        if numerator < 0 and denominator < 0:
            return self.fractionToDecimal(-numerator, -denominator)

        if numerator * denominator < 0:
            return "-" + self.fractionToDecimal(-numerator, denominator)

        if numerator % denominator == 0:
            return str(numerator // denominator)

        if numerator > denominator:
            pre_dot = str(numerator // denominator) + "."
        else:
            pre_dot = "0."

        numerator = numerator % denominator
        digits = []
        remainders = {}

        # Long division:
        while numerator != 0 and numerator not in remainders:
            remainders[numerator] = len(digits)
            numerator *= 10
            while numerator < denominator:
                numerator *= 10
                digits.append("0")

            digits.append(str(numerator // denominator))
            numerator %= denominator

        if numerator != 0:
            ind = remainders[numerator]

            return pre_dot + ''.join(digits[:ind]) + "(" +  ''.join(digits[ind:]) + ")"
        else:
            return pre_dot + ''.join(digits)
