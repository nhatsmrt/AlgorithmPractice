class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        # Space and Space Complexity: O(N)

        # anti-diagnal: r + c = const
        diagonals = {}

        for r in range(len(nums)):
            for c in range(len(nums[r])):
                diag_sum = r + c

                if diag_sum not in diagonals:
                    diagonals[diag_sum] = []

                diagonals[diag_sum].append((r, c))

        ret = []
        for diag_sum in diagonals:
            for coord in reversed(diagonals[diag_sum]):
                ret.append(nums[coord[0]][coord[1]])

        return ret
