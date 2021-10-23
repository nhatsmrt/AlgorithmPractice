class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        # Time Complexity: O(N log(max_ribbons))
        # Space Complexity: O(1)

        low = 1
        high = max(ribbons)

        def cut(ribbons, target_len):
            return sum(map(lambda ribbon: ribbon // target_len, ribbons))


        while low < high:
            mid = high - (high - low) // 2

            num_ribbons = cut(ribbons, mid)
            if num_ribbons < k:
                high = mid - 1
            else:
                low = mid


        if cut(ribbons, low) >= k:
            return low

        return 0
