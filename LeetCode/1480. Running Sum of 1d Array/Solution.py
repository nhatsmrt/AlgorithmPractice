class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return list(itertools.accumulate(nums))
