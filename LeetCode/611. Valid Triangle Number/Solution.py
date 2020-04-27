class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # Time Complexity: O(N^2)
        # Space Complexity: O(1)

        nums.sort()

        ret = 0
        for i in range(2, len(nums)):
            j = 0
            k = i - 1

            while j < k:
                if nums[j] + nums[k] > nums[i]:
                    ret += (k - 1 - j + 1)
                    k -= 1
                else:
                    j += 1

        return ret
