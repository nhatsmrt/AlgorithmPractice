class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # Time Complexity: O(N)
        # Space Complexity: O(1)

        start = 0
        end = 0
        cur = nums[0]

        target = sum(nums) - x
        if not target:
            return len(nums)

        maxLength = -1

        while start < len(nums):
            if end + 1 < len(nums) and nums[end + 1] + cur <= target:
                end += 1
                cur += nums[end]
            else:
                if cur == target:
                    if maxLength == -1 or (end - start + 1) > maxLength:
                        maxLength = end - start + 1

                if start == end:

                    if start + 1 < len(nums):
                        cur = nums[start + 1]
                    end += 1
                    start += 1
                else:
                    cur -= nums[start]
                    start += 1

        if cur == target:
            if maxLength == -1 or (end - start + 1) > maxLength:
                maxLength = end - start + 1

        if maxLength == -1:
            return -1
        return len(nums) - maxLength
