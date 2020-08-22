class Solution:
    def maximumSwap(self, num: int) -> int:
        # Time and Space Complexity: O(N)

        index = [-1] * 10

        digits = self.to_digits(num)
        for i in range(len(digits)):
            index[digits[i]] = i

        for i in range(len(digits)):
            for cand in range(9, digits[i], -1):
                if index[cand] > i:
                    # swap:
                    tmp = digits[i]
                    digits[i] = cand
                    digits[index[cand]] = tmp

                    return self.to_num(digits)

        return num

    def to_digits(self, num: int) -> List[int]:
        if num == 0:
            return [0]

        ret = []
        while num > 0:
            ret.append(num % 10)
            num //= 10

        return ret[::-1]

    def to_num(self, digits: List[int]) -> int:
        ret = 0
        for dig in digits:
            ret = ret * 10 + dig

        return ret
