class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        # Time and space complexity: O((S + sum_i nums[i]) * n)

        self.dp = {}
        return self.find(nums, 0, S)

    def find(self, nums, i, target):
        if i == len(nums):
            return 1 if target == 0 else 0

        if (i, target) in self.dp:
            return self.dp[(i, target)]

        ret = self.find(nums, i + 1, target - nums[i]) + self.find(nums, i + 1, target + nums[i])
        self.dp[(i, target)] = ret
        return ret
