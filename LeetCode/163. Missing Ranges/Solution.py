class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        ret = []
        if len(nums) == 0:
            ret.append(self.to_range(lower, upper))
            return ret

        if lower < nums[0]:
            ret.append(self.to_range(lower, nums[0] - 1))

        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1] - 1:
                ret.append(self.to_range(nums[i] + 1, nums[i + 1] - 1))

        if nums[-1] < upper:
            ret.append(self.to_range(nums[-1] + 1, upper))

        return ret

    def to_range(self, lower: int, upper: int) -> str:
        if lower == upper:
            return str(lower)
        return str(lower) + "->" + str(upper)
