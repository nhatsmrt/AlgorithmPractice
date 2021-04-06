class Solution:
    def minOperations(self, n: int) -> int:
        # Time and Space Complexity: O(1)

        # target: n (median of array)
        # num_operations = sum_{0 <= i < floor(n / 2)} n - (2 * i + 1)
        # = (floor(n / 2)) * (n - 1) - floor(n / 2) * (floor(n / 2) - 1)

        return (n // 2) * (n - 1) - (n // 2) * (n // 2 - 1)
