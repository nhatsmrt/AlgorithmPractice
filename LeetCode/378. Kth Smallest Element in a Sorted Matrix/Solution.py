class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # Time Complexity: O(num_row + K log(num_row))
        # Space Complexity: O(num_row)

        heap = [(matrix[i][0], i) for i in range(len(matrix))]
        heapq.heapify(heap)
        cur_inds = [0 for i in range(len(matrix))]

        for _ in range(k - 1):
            val, row_ind = heapq.heappop(heap)

            if cur_inds[row_ind] + 1 < len(matrix[0]):
                cur_inds[row_ind] += 1
                heapq.heappush(heap, (matrix[row_ind][cur_inds[row_ind]], row_ind))

        return heapq.heappop(heap)[0]
