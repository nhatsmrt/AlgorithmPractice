INF = 1000000000


class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        # Time and Space Complexity: O(N)

        if len(A) == 1:
            return A[0]

        max_subarr = []
        S = 0

        for i in range(len(A)):
            if S + A[i] > 0:
                S += A[i]
                max_subarr.append(S)
            else:
                S = 0
                max_subarr.append(-INF)

        candidate1 = max(max(max_subarr), max(A))

        prefixes = [A[0]]
        for i in range(1, len(A)):
            prefixes.append(A[i] + prefixes[-1])

        suffixes = [A[-1]]
        for i in range(len(A) - 2, -1, -1):
            suffixes.append(A[i] + suffixes[-1])

        for i in range(1, len(A)):
            prefixes[i] = max(prefixes[i], prefixes[i - 1])
            suffixes[i] = max(suffixes[i], suffixes[i - 1])

        return max(candidate1, max(prefixes[i] + suffixes[len(A) - i - 2] for i in range(len(A) - 1)))
