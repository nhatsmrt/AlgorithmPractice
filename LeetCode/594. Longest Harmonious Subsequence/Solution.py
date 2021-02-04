class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # Time and Space Complexity: O(N)

        cnter = Counter(nums)

        ret = 0
        for val in cnter:
            if cnter[val + 1]:
                ret = max(cnter[val] + cnter[val + 1], ret)

        return ret
