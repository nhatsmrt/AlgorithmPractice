class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        cur = 0

        while cur < len(bits):
            if bits[cur] == 1:
                if cur == len(bits) - 2:
                    return False
                else:
                    cur += 2
            else:
                if cur == len(bits) - 1:
                    return True
                else:
                    cur += 1
