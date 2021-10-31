class Solution:
    def splitArray(self, nums: List[int]) -> bool:
        # Time Complexity: O(N^2)
        # Space Complexity: O(N)

        prefixes = list(accumulate(nums))

        # range of j: 3 to n - 3
        def range_sum(start, end):
            if start == 0:
                return prefixes[end]

            return prefixes[end] - prefixes[start - 1]

        def split(start, end):
            ret = set()

            for split_ind in range(start + 1, end):
                left = range_sum(start, split_ind - 1)
                right = range_sum(split_ind + 1, end)

                if left == right:
                    ret.add(left)

            return ret


        for j in range(3, len(nums) - 3):
            if split(0, j - 1).intersection(split(j + 1, len(nums) - 1)):
                return True

        return False
