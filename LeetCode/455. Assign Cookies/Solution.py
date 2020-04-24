class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # Greedy strategy: always gives cookies to the less greedy first
        # using the smalles cookie possible

        # Proof: Suppose an optimal assignment for remaining children is
        # (g_i1, ..., g_ik). If g_i1 is the least greedy of all children
        # then we are done. Otherwise, we can always replace it by a least greedy children
        # with no reduction in the number of children fed.

        g.sort()
        s.sort()

        ret = 0
        i = 0
        j = 0

        while i < len(g) and j < len(s):
            while j < len(s) and g[i] > s[j]:
                j += 1

            if j == len(s):
                return ret

            ret += 1
            i += 1
            j += 1

        return ret
        
