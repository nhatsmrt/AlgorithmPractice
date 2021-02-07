class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        # Time and Space Complexity: O(N)

        occs = []

        for i, ch in enumerate(s):
            if ch == c:
                occs.append(i)

        ret = []

        for i, occ in enumerate(occs):
            if i == 0:
                start = 0
            else:
                start = occs[i] - (occs[i] - occs[i - 1]) // 2


            if i == len(occs) - 1:
                end = len(s) - 1
            else:
                end = occs[i + 1] - (occs[i + 1] - occs[i]) // 2 - 1

            for j in range(start, end + 1):
                ret.append(abs(occ - j))

        return ret
        
