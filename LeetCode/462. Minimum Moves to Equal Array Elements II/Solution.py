from random import randint


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        # f(x) = \sum_i |x - a_i|
        # Suppose a_i's are sorted. Then for x < median,
        # increase x decrease f
        # and for x > median, decrease x decrease f
        # So minima is (one) of the median

        median = self.find_median(nums, 0, len(nums) - 1, len(nums) // 2)
        return sum(abs(num - median) for num in nums)

    def find_median(self, nums: List[int], start: int, end: int, k: int) -> int:
        # QuickSelect. Average time complexity: O(N)
        if start == end:
            return nums[start]

        # random pivot
        self.swap(nums, randint(start, end), end)

        last_smaller = start - 1
        for i in range(start, end):
            if nums[i] < nums[end]:
                self.swap(nums, last_smaller + 1, i)
                last_smaller += 1

        self.swap(nums, last_smaller + 1, end)
        # pivot is at last_smaller + 1
        left_size = last_smaller + 1 - start + 1
        if left_size == k + 1:
            return nums[last_smaller + 1]
        elif left_size > k + 1:
            return self.find_median(nums, start, last_smaller + 1, k)
        else:
            return self.find_median(nums, last_smaller + 2, end, k - left_size)

    def swap(self, nums: List[int], i: int, j: int):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp
