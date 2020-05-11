class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        # Time complexity: O(N log N)
        # Space complexity: O(N)

        A.sort()

        for i in range(len(A) - 1, 1, -1):
            if A[i] < A[i - 1] + A[i - 2]:
                return A[i] + A[i - 1] + A[i - 2]

        return 0
