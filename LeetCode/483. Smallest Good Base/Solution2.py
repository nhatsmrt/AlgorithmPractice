class Solution:
    def smallestGoodBase(self, n: str) -> str:
        # Time Complexity:
        # O(sum_{length = 2}^{log(x)} log(x^{1 / (length - 1)} - x^{1 / length}))
        # (Conjecture): = O(log N)
        # Space Complexity: O(1)

        n = int(n)

        for length in range(len(bin(n)) - 2, 1, -1):
            base = self.is_feasible(n, length)
            if base != -1:
                return str(base)

    def is_feasible(self, num: int, length: int) -> int:
        # (base^length - 1) // (base - length) = num
        # base^{length - 1} + ... + 1 = num
        #  base^length >= num >= base^{length - 1}
        # num^{1/(length - 1)} >= base >= num^{1/(length)}

        base_low = max(2, int(math.pow(num, 1 / length)))

        if length > 2:
            base_high = int(math.pow(num, 1 / (length - 1)))
        else:
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

        if length == 2:
            print(math.pow(num, 1 / (length - 1)))
            print(base_low)
        if num * (base_low - 1) == (base_low ** length - 1):
            return base_low

        return -1
