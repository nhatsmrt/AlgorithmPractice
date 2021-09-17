class Solution:
    def minDifference(self, nums: List[int]) -> int:
        # Time Complexity: O(N)
        # Space Complexity: O(1)

        if len(nums) <= 4:
            return 0

        top_four = [None] * 4
        bottom_four = [None] * 4

        for val in nums:
            for i, bot_val in enumerate(bottom_four):
                if bot_val is None or val <= bot_val:
                    bottom_four[i:] = [val] + bottom_four[i:3]
                    break

            for i, top_val in enumerate(top_four):
                if top_val is None or val >= top_val:
                    top_four[i:] = [val] + top_four[i:3]
                    break

        ret = None
        for top_change in range(4):
            bottom_change = 3 - top_change
            arr_range = abs(top_four[top_change] - bottom_four[bottom_change])

            if ret is None or ret > arr_range:
                ret = arr_range

        return ret
