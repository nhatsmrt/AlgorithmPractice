class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        # Time Complexity: O(n log m)
        # Space Complexity: O(1)

        # Search space invariant: row r1 to row r2
        # such that there exists c1, c2 satisfying:
        # for all c: mat[r1][c1] > mat[r1 - 1][c]; mat[r2][c2] > mat[r2 + 1][c]
        # when r1 + 1 <= r2, maximum of search space is a ''peak element''

        # We can reduce the search space by repeatedly considered the middle row
        # and its two neighboring row, finding the max entry among these 3 rows
        # If the max entry is in the middle row - we find a peak element
        # Otherwise, if it's in the left row, consider the left half + middle column
        # and if it's in the right row, consider the right half + middle column

        def find_largest(low, high):
            ret = None

            for i in range(low, high + 1):
                for j in range(len(mat[0])):
                    if ret is None or mat[i][j] > mat[ret[0]][ret[1]]:
                        ret = i, j

            return ret

        low, high = 0, len(mat) - 1

        while low + 1 < high:
            mid = (low + high) // 2

            i, j = find_largest(mid - 1, mid + 1)

            if i == mid:
                return [i, j]
            elif i == mid - 1:
                high = mid
            else:
                low = mid

        return list(find_largest(low, high))
