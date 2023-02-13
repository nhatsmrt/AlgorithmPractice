def compute_longest_streak_from(val, longest_streak_from, values):
    if val not in values:
        return 0

    if val in longest_streak_from:
        return longest_streak_from[val]

    longest_streak_from[val] = 1 + compute_longest_streak_from(val ** 2, longest_streak_from, values)
    return longest_streak_from[val]

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        # Time and Space Complexity: O(N)

        values = set(nums)
        adj_list = {}

        longest_streak_from = {}
        for val in values:
            compute_longest_streak_from(val, longest_streak_from, values)

        ret = max(longest_streak_from.values())
        return ret if ret >= 2 else -1
