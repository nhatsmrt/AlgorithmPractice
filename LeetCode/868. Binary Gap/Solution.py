class Solution:
    def binaryGap(self, n: int) -> int:
        # Time Complexity: O(log N)
        # Space Complexity: O(1)

        ret = 0
        lastOcc = -1
        i = 0

        while n > 0:
            if n & 1:
                if lastOcc >= 0:
                    ret = max(i - lastOcc, ret)

                lastOcc = i

            i += 1
            n >>= 1

        return ret
                    
