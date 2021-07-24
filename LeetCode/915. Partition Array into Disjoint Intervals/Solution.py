class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        # Time and Space Complexity: O(N)
        maxes = list(accumulate(nums, lambda a, b: max(a, b)))
        mins = list(reversed(list(accumulate(reversed(nums), lambda a, b: min(a, b)))))

        for i in range(len(nums) - 1):
            if maxes[i] <= mins[i + 1]:
                return i + 1
