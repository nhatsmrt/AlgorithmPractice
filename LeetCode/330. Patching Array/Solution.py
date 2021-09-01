class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        # Time Complexity: O(|nums| log |nums| + log n)
        # Space Complexity: O(1)

        # Idea: consider each number in nums in sorted order
        # at any point, suppose we have covered [1, first_missing)
        # if num <= first_missing, we can simply add it to the considered set
        # raising first missing value to first_missing + num

        # Otherwise, adding num (or any number larger than it in nums) won't help;
        # we have to add a number <= first_missing;
        # notice that adding first_missing would be as good as adding any smaller number
        # raising the first missing value to first_missing * 2

        nums.sort()

        first_missing = 1
        i = 0
        ret = 0

        while first_missing < n + 1:
            if i < len(nums):
                if first_missing < nums[i]: # add first_missing
                    first_missing *= 2
                    ret += 1
                else:
                    first_missing += nums[i]
                    i += 1
            else: # add covered
                first_missing *= 2
                ret += 1


        return ret
