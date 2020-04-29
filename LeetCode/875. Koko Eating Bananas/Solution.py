class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        low = 1
        high = max(piles)

        while low < high:
            mid = low + (high - low) // 2

            time = sum(map(
                lambda pile : pile // mid if pile % mid == 0 else pile // mid + 1,
                piles
            ))

            if time > H:
                low = mid + 1
            else:
                high = mid


        return low
        
