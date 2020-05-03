class Solution:
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        # Time Complexity: O(N log(sum(sweetness)))
        # Space Complexity: O(1)

        high = sum(sweetness)
        low = 1

        while low < high:
            mid = high - (high - low) // 2

            if not self.isPossible(sweetness, mid, K):
                high = mid - 1
            else:
                low = mid

        return low



    def isPossible(self, sweetness: List[int], target: int, K: int) -> int:
        cur = 0
        num_parts = 0

        for val in sweetness:
            if cur + val >= target:
                cur = 0
                num_parts += 1
            else:
                cur += val

        return num_parts >= K + 1
        
