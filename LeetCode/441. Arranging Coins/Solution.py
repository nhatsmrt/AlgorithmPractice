class Solution:
    def arrangeCoins(self, n: int) -> int:
        low = 0
        high = n

        while low < high:
            mid = high - (high - low) // 2
            cand = mid * (mid + 1) // 2

            if cand == n:
                return mid
            elif cand < n:
                low = mid
            else:
                high = mid - 1

        return low

        
