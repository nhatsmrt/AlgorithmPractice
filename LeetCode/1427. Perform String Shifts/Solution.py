class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        offset = 0
        for sh in shift:
            if sh[0] == 0:
                offset += sh[1]
            else:
                offset -= sh[1]

        offset %= len(s)
        return s[offset:] + s[:offset]
