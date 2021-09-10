class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        # Time Complexity: O(KM log KM)

        seen = set()
        moves = []

        for i in range(len(mat)):
            moves.append([0] * i + [1] + [0] * (len(mat) - i - 1))

        initial_state = (0,) * len(mat)
        initial_val = sum(mat[i][initial_state[i]] for i in range(len(mat)))
        consideration = [(initial_val, initial_state)]
        seen.add(initial_state)

        for _ in range(k - 1):
            val, state = heapq.heappop(consideration)

            for i in range(len(mat)):
                if state[i] + 1 < len(mat[0]):
                    new_state = state[:i] + (state[i] + 1,) + state[i + 1:]

                    if new_state not in seen:
                        seen.add(new_state)
                        new_val = val - mat[i][state[i]] + mat[i][new_state[i]]

                        heapq.heappush(consideration, (new_val, new_state))

        return consideration[0][0]
