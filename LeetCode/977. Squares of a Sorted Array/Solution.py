class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:

        i = 0
        while i < len(A) and A[i] < 0:
            i += 1

        if i == 0:
            return [val ** 2 for val in A]

        j = i - 1
        ret = []
        while j >= 0 and i < len(A):
            if A[i] ** 2 < A[j] ** 2:
                ret.append(A[i] ** 2)
                i += 1
            else:
                ret.append(A[j] ** 2)
                j -= 1


        for k in range(i, len(A)):
            ret.append(A[k] ** 2)

        for k in range(j, -1, -1):
            ret.append(A[k] ** 2)

        return ret
