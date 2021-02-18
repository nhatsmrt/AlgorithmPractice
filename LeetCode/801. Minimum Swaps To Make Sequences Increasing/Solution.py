class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        # Time and Space Complexity: O(N)

        if len(A) == 1:
            return 0

        self.dp = [[-1 for j in range(2)] for i in range(len(A))]
        return min(self.find_min_swap(A, B, 1, 0), 1 + self.find_min_swap(A, B, 1, 1))

    def find_min_swap(self, A: List[int], B: List[int], i: int, last_swapped: int):
        if i == len(A):
            return 0

        if self.dp[i][last_swapped] >= 0:
            return self.dp[i][last_swapped]

        last_A = B[i - 1] if last_swapped else A[i - 1]
        last_B = A[i - 1] if last_swapped else B[i - 1]

        candidates = []
        # case 1: swap:
        if B[i] > last_A and A[i] > last_B:
            candidates.append(1 + self.find_min_swap(A, B, i + 1, 1))

        # case 2: not swap:
        if A[i] > last_A and B[i] > last_B:
            candidates.append(self.find_min_swap(A, B, i + 1, 0))

        ret = min(candidates)
        self.dp[i][last_swapped] = ret
        return ret
