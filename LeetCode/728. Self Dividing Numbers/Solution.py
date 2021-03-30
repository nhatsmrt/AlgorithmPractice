class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ret = []

        for num in range(left, right + 1):
            tmp = num

            while tmp > 0:
                dig = tmp % 10

                if dig == 0 or num % dig:
                    break

                tmp //= 10
            else:
                ret.append(num)

        return ret
