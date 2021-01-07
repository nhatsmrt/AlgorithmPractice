class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # Time Complexity: O(log N)
        # Space Complexity: O(1)

        if arr[0] > k:
            return k

        low = 0
        high = len(arr) - 1

        while low < high:
            mid = high - (high - low) // 2

            num_missing = arr[mid] - mid - 1

            if num_missing >= k:
                high = mid - 1
            else:
                low = mid

        offset = k - (arr[low] - low - 1)
        return arr[low] + offset
                
