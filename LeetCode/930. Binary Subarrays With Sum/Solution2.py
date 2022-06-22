class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # Time Complexity: O(N)
        # Space Complexity: O(1)

        start = -1
        end = -1
        snd = 0
        low_sum = 0
        high_sum = nums[0]

        ret = 0
        while start < len(nums) and snd < len(nums):
            if low_sum + goal < high_sum:
                start = end + 1
                end += 1

                if end < len(nums):
                    low_sum += nums[end]
            elif end + 1 < len(nums) and nums[end + 1] == 0:
                end += 1
            elif high_sum - low_sum < goal:
                snd += 1
                if snd < len(nums):
                    high_sum += nums[snd]
            else:
                if high_sum - low_sum == goal:
                    if snd <= end:
                        ret += (snd - 1) - start + 1
                    else:
                        ret += end - start + 1

                    snd += 1
                    if snd < len(nums):
                        high_sum += nums[snd]

        return ret
