def range_sum(begin, end, prefixes):
    return prefixes[end] - prefixes[begin]

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        # Time and Space Complexity: O(N)

        prefixes = [0] + list(accumulate(nums))
        rotations = []

        # first rotation:
        first = sum(i * num for i, num in enumerate(nums))
        rotations.append(first)

        for i in range(1, len(nums)):
            delta = range_sum(0, len(nums) - i, prefixes) \
            + range_sum(len(nums) - i + 1, len(nums), prefixes) \
            - nums[-i] * (len(nums) - 1)

            new_rotation = rotations[-1] + delta

            rotations.append(new_rotation)

        return max(rotations)
