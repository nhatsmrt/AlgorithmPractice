class Solution:
    def numberOfSteps (self, num: int) -> int:
        # Time Complexity: O(W) = O(log N)
        # Space Complexity: O(1)

        ret = 0

        while num > 1:
            if num & 1:
                ret += 2
            else:
                ret += 1

            num >>= 1

        if num == 1:
            ret += 1

        return ret
