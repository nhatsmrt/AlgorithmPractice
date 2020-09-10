class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        # Time Complexity: O(N)
        # Space Complexity: O(1)

        expected_sum = (arr[0] + arr[-1]) * (len(arr) + 1) // 2
        return expected_sum - sum(arr)
