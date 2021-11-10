class Solution:
    def maximum69Number (self, num: int) -> int:
        # Time Complexity: O(W)
        # Space Complexity: O(1)

        ret = 0
        changed = False

        for dig in str(num):
            ret *= 10

            if not changed and dig == "6":
                ret += 9
                changed = True
            else:
                ret += int(dig)

        return ret
