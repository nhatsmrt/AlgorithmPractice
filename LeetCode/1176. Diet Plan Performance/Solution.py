class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        # Time and Space Complexity: O(N)

        prefixes = [0] + list(itertools.accumulate(calories))

        ret = 0
        for i in range(len(prefixes) - k):
            window_sum = prefixes[i + k] - prefixes[i]

            if window_sum > upper:
                ret += 1
            elif window_sum < lower:
                ret -= 1

        return ret
