class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Time Complexity: O(N)
        # Space Complexity: no extra space

        for num in nums:
            nums[abs(num) - 1] = -abs(nums[abs(num) - 1])

        ret = []
        for i in range(1, len(nums) + 1):
            if nums[i - 1] > 0:
                ret.append(i)

        return ret
        
