class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        bitmask = reduce(lambda x, y: x^y, nums)
        x_check = bitmask & (-bitmask)
        x = reduce(lambda x, y: x^y, filter(lambda x: x & x_check, nums))
        y = bitmask ^ x

        return [x, y]
