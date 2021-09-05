class Solution:
    def kthSmallestPrimeFraction(self, A: List[int], K: int) -> List[int]:
        # Time Complexity: O(K log N + N)
        # Space Complexity: O(N)

        index = [len(A) - 1] * len(A)
        candidates = [(A[i] / A[-1], i) for i in range(len(A))]
        heapq.heapify(candidates)

        for _ in range(K - 1):
            _, num_index = heapq.heappop(candidates)
            if index[num_index] > num_index:
                index[num_index] -= 1
                value = A[num_index] / A[index[num_index]]

                heapq.heappush(candidates, (value, num_index))

        return [A[candidates[0][1]], A[index[candidates[0][1]]]]
