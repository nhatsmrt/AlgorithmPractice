class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        # Time Complexity: O(N)
        # Space Complexity: O(1)

        if len(A) <= 1:
            return len(A)

        start = 0
        ret = 1

        while start + 1 < len(A):
            if A[start + 1] != A[start]:
                end = start + 2

                while end < len(A) and (A[end] - A[end - 1]) * (A[end - 1] - A[end - 2]) < 0:
                    end += 1

                ret = max(ret, end - start)

                start = end - 1
            else:
                start += 1

        return ret
        
