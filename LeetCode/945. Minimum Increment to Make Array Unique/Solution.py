class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        # Time Complexity: O(N log N)
        # Space Complexity: O(sort)

        A.sort()
        cur_max = -1
        ret = 0

        for num in A:
            if num > cur_max:
                cur_max = num
            else:
                ret += cur_max + 1 - num
                cur_max += 1

        return ret
