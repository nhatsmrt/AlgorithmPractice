class Solution:
    def smallestGoodBase(self, n: str) -> str:
        # Time Complexity: O(log(n)^2)
        # Space Complexity: O(1)
        n = int(n)

        for length in range(len(bin(n)) - 1, 1, -1):
            base = self.is_feasible(n, length)
            if base != -1:
                return str(base)

    def is_feasible(self, num: int, length: int) -> bool:
        base_low = 2
        base_high = num

        while base_low < base_high:
            mid = base_low + (base_high - base_low) // 2
            diff = num * (mid - 1) - (mid ** length - 1)

            if diff == 0:
                return mid
            elif diff < 0:
                # base is too high:
                base_high = mid - 1
            else:
                # base is too low:
                base_low = mid + 1

        if num * (base_low - 1) == (base_low ** length - 1):
            return base_low

        return -1


        
