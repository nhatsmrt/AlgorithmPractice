class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # Idea: use nums[abs(num) - 1] as the flag for num

        for num in nums:
            nums[abs(num) - 1] = -nums[abs(num) - 1]

        ret = []
        for num in nums:
            if nums[abs(num) - 1] > 0:
                ret.append(abs(num))
                nums[abs(num) - 1] = -nums[abs(num) - 1]

        return ret
