class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        low = 0
        high = len(A) - 1

        # Ternary search to find Peak:
        while low < high:

            m1 = low + (high - low) // 3
            m2 = high - (high - low) // 3

            v1 = A[m1]
            v2 = A[m2]

            if v1 == v2:
                low = m1 + 1
                high = m2 - 1
            elif v1 < v2:
                low = m1 + 1
            else:
                high = m2 - 1

        return low

        
