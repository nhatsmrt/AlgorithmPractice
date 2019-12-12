class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        return self.search(nums, 0, len(nums) - 1)

    def search(self, nums: List[int], start: int, end: int) -> int:
        if start == end:
            return nums[start]

        mid = (start + end) // 2
        if (
            (mid == start or nums[mid - 1] != nums[mid]) and
            (mid == end or nums[mid + 1] != nums[mid])
        ):
            return nums[mid]

        if mid != start and nums[mid] == nums[mid - 1]:
            if mid % 2 == 0:
                return self.search(nums, start, mid - 2)
            else:
                return self.search(nums, mid + 1, end)

        if mid % 2 == 0:
            return self.search(nums, mid + 2, end)

        return self.search(nums, start, mid - 1)
