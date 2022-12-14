def can_build(s: str, i: int, last: int, solutions) -> bool:
    if i == len(s):
        return True

    key = (i, last)

    if key in solutions:
        return solutions[key]

    cand = 0
    cur = i

    while cand <= last - 1 and cur < len(s):
        cand = cand * 10 + int(s[cur])

        if cand == last - 1 and can_build(s, cur + 1, last - 1, solutions):
            # found!
            ret = True
            break

        cur += 1
    else:
        ret = False

    solutions[key] = ret
    return ret


class Solution:
    def splitString(self, s: str) -> bool:
        # Space Complexity: O(N^2)
        # Time Complexity: O(N^3)
        solutions = {}
        first = 0

        for i in range(0, len(s) - 1):
            first = first * 10 + int(s[i])
            if can_build(s, i + 1, first, solutions):
                return True

        return False
