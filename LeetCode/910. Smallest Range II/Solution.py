class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        # Time Complexity: O(N log N)
        # Space Complexity: O(|sorting|)

        # Suppose the array is sorted

        # Observation 1: answer <= max(A) - min(A)
        # since worst case scenario, we can shift entire A by K

        # Observation 2: in a solution where answer < max(A) - min(A),
        # if A[i] < A[j], and A[i], A[j] go separate direction
        # then A[i] goes up, and A[j] goes down

        # This mean that: 0 -> i goes up, and i + 1 -> len(A) - 1 goes down,
        # for some i

        # Also note that after shifting, B[0] <= B[1]... <= B[i]
        # and B[i + 1] <= ... <= B[-1]
        # so for min range, we only need to consider B[0] and B[i + 1]
        # and for max_range, we only need to consider B[-1] and B[i]


        if len(A) == 1 or K == 0:
            return max(A) - min(A)

        A.sort()

        ret = A[-1] - A[0]

        shifted_first = A[0] + K
        shifted_last = A[-1] - K

        for i in range(0, len(A) - 1):
            low = min(A[i + 1] - K, shifted_first)
            high = max(A[i] + K, shifted_last)

            ret = min(ret, high - low)



        return ret
    
