class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        ret = 0
        counts = Counter(nums)

        for num in counts:
            if counts[num] == 1:
                ret += num

        return ret
