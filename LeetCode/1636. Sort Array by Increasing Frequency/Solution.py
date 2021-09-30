class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        cnter = Counter(nums)
        return sorted(nums, key=lambda val: (cnter[val], -val))
