import math

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        # Mo's Algorithm
        # Time Comlexity: O((N + Q) * sqrt(N))
        # Space Complexity: O(Q)

        block_size = math.sqrt(len(arr))

        queries = [(queries[i][0], queries[i][1], i) for i in range(len(queries))]
        queries.sort(key=lambda q:q[1])
        queries.sort(key=lambda q:q[0] // block_size)

        ret = [-1] * len(queries)
        # Complete first query:
        L, R, ind = queries[0]
        cumXor = 0

        for i in range(L, R + 1):
            cumXor ^= arr[i]

        ret[ind] = cumXor

        for i in range(1, len(queries)):
            newL, newR, ind = queries[i]

            lowerL = min(newL, L)
            upperL = max(newL, L)
            lowerR = min(newR, R)
            upperR = max(newR, R)

            for i in range(lowerL, upperL):
                cumXor ^= arr[i]

            for i in range(lowerR + 1, upperR + 1):
                cumXor ^= arr[i]

            ret[ind] = cumXor
            L, R = newL, newR

        return ret
