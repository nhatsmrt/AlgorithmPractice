class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # Time Complexity: O(N log N)
        # Space Complexity: O(N)

        expected = sorted(heights)

        expected_ind = {}

        for i, height in enumerate(expected):
            if height not in expected_ind:
                expected_ind[height] = set()

            expected_ind[height].add(i)

        ret = 0
        for i, height in enumerate(heights):
            if i not in expected_ind[height]:
                ret += 1

        return ret
