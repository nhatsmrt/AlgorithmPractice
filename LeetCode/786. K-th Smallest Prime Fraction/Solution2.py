class Solution:
    def kthSmallestPrimeFraction(self, A: List[int], K: int) -> List[int]:
        # Time Complexity: O(N log W)
        # Space Complexity: O(1)

        low = 0
        high = A[-1]

        def get_rank(value):
            rank = 0
            floor = None
            denom_ind = 0

            for num_ind in range(len(A)):
                while denom_ind < len(A) and A[num_ind] / A[denom_ind] > value:
                    denom_ind += 1

                rank += len(A) - denom_ind
                if denom_ind < len(A):
                    if floor is None or A[floor[0]] / A[floor[1]] < A[num_ind] / A[denom_ind]:
                        floor = [num_ind, denom_ind]

            return rank, floor


        while True:
            mid = (low + high) / 2
            rank, floor = get_rank(mid)

            if rank == K:
                return A[floor[0]], A[floor[1]]
            elif rank < K:
                low = mid
            else:
                high = mid
