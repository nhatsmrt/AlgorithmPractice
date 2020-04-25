class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        prefixes = [0]
        for num in A:
            prefixes.append(prefixes[-1] + num)

        ret = 0
        largest_right_sum = 0

        for i in range(len(A) - L, M - 1, -1):
            largest_right_sum = max(largest_right_sum, prefixes[i + L] - prefixes[i])
            ret = max(ret, prefixes[i] - prefixes[i - M] + largest_right_sum)

        largest_right_sum = 0
        for i in range(len(A) - M, L - 1, -1):
            largest_right_sum = max(largest_right_sum, prefixes[i + M] - prefixes[i])
            ret = max(ret, prefixes[i] - prefixes[i - L] + largest_right_sum)

        return ret
