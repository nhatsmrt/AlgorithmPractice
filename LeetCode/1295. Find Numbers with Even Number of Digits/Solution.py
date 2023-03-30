def num_digit(number):
    ret = 0

    while number > 0:
        ret += 1
        number //= 10

    return ret

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return len(list(filter(lambda l: l % 2 == 0, map(num_digit, nums))))
