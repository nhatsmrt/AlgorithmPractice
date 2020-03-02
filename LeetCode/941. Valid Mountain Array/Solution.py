class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False
        i = 0
        while i < len(A) - 1:
            if A[i] == A[i + 1]:
                return False
            elif A[i] < A[i + 1]:
                i += 1
            else:
                break

        if i == len(A) - 1 or i == 0:
            return False

        while i < len(A) - 1:
            if A[i] <= A[i + 1]:
                return False
            i += 1

        return True
