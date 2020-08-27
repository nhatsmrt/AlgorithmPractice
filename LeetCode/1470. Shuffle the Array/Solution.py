class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ret = []
        for i in range(n):
            ret.append(nums[i])
            ret.append(nums[i + n])

        return ret
