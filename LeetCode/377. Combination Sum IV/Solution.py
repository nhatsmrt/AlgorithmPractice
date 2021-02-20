class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # Time Complexity: O(target * N)
        # Space Complexity: O(target)

        self.dp = {}
        return self.build(nums, target)

    def build(self, nums: List[int], target: int) -> int:
        if target in self.dp:
            return self.dp[target]

        ret = 0

        if target:
            for num in nums:
                if num <= target:
                    ret += self.build(nums, target - num)
        else:
            ret += 1

        self.dp[target] = ret
        return ret
