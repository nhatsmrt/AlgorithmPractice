class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # Time Complexity: O(N)
        # Space Complexity: O(1)

        max_3 = [None] * 3
        min_2 = [None] * 2

        for num in nums:
            for i in range(3):
                if max_3[i] is None or max_3[i] < num:
                    max_3 = max_3[:i] + [num] + max_3[i:2]
                    break

            for i in range(2):
                if min_2[i] is None or min_2[i] > num:
                    min_2 = min_2[:i] + [num] + min_2[i:1]
                    break

        return max(min_2[0] * min_2[1] * max_3[0], max_3[0] * max_3[1] * max_3[2])
