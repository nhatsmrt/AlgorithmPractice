import bisect


class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        # Time Complexity: O(N^2)
        # Space Complexity: O(1)
        nums.sort()
        ret = 0

        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                while j < k and nums[i] + nums[j] + nums[k] >= target:
                    k -= 1

                if j < k:
                    ret += (k - j)

                j += 1

        return ret
