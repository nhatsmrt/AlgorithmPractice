class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # Time Complexity: O(log N) = O(W)
        # Space Complexity: O(1)

        low = 1
        high = num - 1

        while low < high:
            mid = low + (high - low) // 2

            if mid * mid == num:
                return True
            elif mid * mid < num:
                low = mid + 1
            else:
                high = mid - 1

        return low * low == num
        
