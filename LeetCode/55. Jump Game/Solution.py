class Solution:
    def canJump(self, nums: List[int]) -> bool:
        start = 0
        end = 0

        while end < len(nums) - 1:
            newEnd = end
            for i in range(start, end + 1):
                newEnd = max(newEnd, i + nums[i])

            if newEnd == end:
                return False

            start = end + 1
            end = newEnd

        return True
        
