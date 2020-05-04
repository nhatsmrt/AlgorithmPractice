class Solution:
    def findComplement(self, num: int) -> int:
        if num == 0:
            return 1

        ret = 0
        i = 0

        while num > 0:
            ret += ((num & 1) ^ 1) << i
            i += 1
            num >>= 1

        return ret
