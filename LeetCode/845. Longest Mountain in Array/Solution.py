class Solution:
    def longestMountain(self, A: List[int]) -> int:
        # Time Complexity: O(N)
        # Space Complexity: O(1)

        ret = 0
        start = 0
        peak = start
        end = -1

        while start < len(A):
            if start + 1 < len(A) and A[start + 1] <= A[start]:
                start += 1
                peak = start
                end = start
            elif peak + 1 < len(A) and A[peak + 1] > A[peak]:
                peak += 1
                end = peak
            elif end + 1 < len(A) and A[end + 1] < A[end]:
                end += 1
            else:
                if peak > start and end > peak:
                    ret = max(ret, end - start + 1)

                if end > peak:
                    start = end
                    peak = end
                else:
                    start = end + 1
                    peak = end + 1
                    end += 1

        return ret
