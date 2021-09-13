class Solution:
    def solve(self, nums):
        # Time Complexity: T(n) = O(n log n)
        # T(n) = T(k) + T(n - k) + O(min(k, n - k))
        # Space Complexity: O(n)

        # Idea 1: If a subarray has no unique elements, then result is False
        # Idea 2: Otherwise, if A[L:R + 1] has unique element A[k]
        # then we need to check A[L:k] and A[k + 1:R + 1]

        # To find such A[k], we alternate between checking the left and the right ends of the array
        # This would take O(min(k, n - k))

        # Uniqueness of A[k] within A[L:R + 1] can be check
        # by 2 auxiliary arrays indicating the next and previous
        # occurences of A[k].

        self.next = [None] * len(nums)
        self.prev = [None] * len(nums)

        index = {}

        for i, val in enumerate(nums):
            if val in index:
                self.next[index[val]] = i

            index[val] = i

        index = {}
        for i in range(len(nums) - 1, -1, -1):
            val = nums[i]

            if val in index:
                self.prev[index[val]] = i

            index[val] = i

        return self.check(nums, 0, len(nums) - 1)

    def is_unique(self, i, start, end):
        next, prev = self.next[i], self.prev[i]

        return (next is None or next > end) and (prev is None or prev < start)

    def check(self, nums, start, end):
        if start >= end:
            return True

        i = start
        j = end

        while i <= j:
            if self.is_unique(i, start, end):
                return self.check(nums, start, i - 1) and self.check(nums, i + 1, end)
            elif self.is_unique(j, start, end):
                return self.check(nums, start, j - 1) and self.check(nums, j + 1, end)

            i += 1
            j -= 1

        return False
