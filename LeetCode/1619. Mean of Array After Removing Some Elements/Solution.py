class Solution:
    def trimMean(self, arr: List[int]) -> float:
        # Time Complexity: O(N log N)
        # Space Complexity: O(1)

        arr.sort()
        trim_len = len(arr) // 20

        return sum(arr[trim_len:len(arr) - trim_len]) / (len(arr) - 2 * trim_len)
