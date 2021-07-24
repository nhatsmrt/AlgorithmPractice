class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        # Time and Space Complexity: O(N)
        maxes = accumulate(nums, lambda a, b: max(a, b))
        mins = iter(reversed(list(accumulate(reversed(nums), lambda a, b: min(a, b)))))

        next(mins)
        for i, (prefix_max, suffix_min) in enumerate(zip(maxes, mins)):
            if prefix_max <= suffix_min:
                return i + 1
