class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        bound = min(len(a), len(b))
        ret = []

        for i in range(bound):
            a_dig = int(a[len(a) - 1 - i])
            b_dig = int(b[len(b) - 1 - i])

            sum_dig = a_dig + b_dig + carry
            ret.append(str(sum_dig % 2))
            carry = sum_dig // 2

        for i in range(bound, len(a)):
            a_dig = int(a[len(a) - 1 - i])
            sum_dig = a_dig + carry
            carry = sum_dig // 2
            ret.append(str(sum_dig % 2))

        for j in range(bound, len(b)):
            b_dig = int(b[len(b) - 1 - j])
            sum_dig = b_dig + carry
            carry = sum_dig // 2
            ret.append(str(sum_dig % 2))

        if carry == 1:
            ret.append(str(1))

        return ''.join(ret[::-1])


        
