class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        # Time Complexity: O(N log N) (N is total number of elements)
        # Space Complexity: O(N)

        # anti-diagnal: r + c = const
        ret = []
        pq = [(row, 0, row) for row in range(len(nums))]
        heapq.heapify(pq)

        while pq:
            diag_const = pq[0][0]

            diag = []
            while pq and pq[0][0] == diag_const:
                diag.append(heapq.heappop(pq))

            for _, col, row in diag:
                if col + 1 < len(nums[row]):
                    heapq.heappush(pq, (row + col + 1, col + 1, row))


            ret.extend(nums[row][col] for _, col, row in diag)

        return ret
