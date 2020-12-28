class Solution:
    def reachNumber(self, target: int) -> int:
        # Time Complexity: O(log |target|)
        # Space Complexity: O(1)

        if not target:
            return 0

        if target < 0:
            return self.reachNumber(-target)

        # n * (n + 1) // 2 - target = 2 * x
        # n * (n + 1) = 2 * target + 4 * x

        low = 1
        high = 2

        target *= 2

        while high * (high + 1) < target:
            low = high
            high *= 2

        while low < high:
            mid = low + (high - low) // 2
            sum_double = mid * (mid + 1)

            if sum_double < target:
                low = mid + 1
            else:
                high = mid

        while ((low + 1) * low - target) % 4:
            low += 1

        return low
