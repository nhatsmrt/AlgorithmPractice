def min_flips(s, ind, prev, solutions):
    if ind == len(s):
        return 0

    if solutions[ind][prev] >= 0:
        return solutions[ind][prev]

    cur = int(s[ind])

    if prev == 0:
        # flip or not flip is fine!
        ret = min(
            min_flips(s, ind + 1, cur, solutions),
            1 + min_flips(s, ind + 1, 1 - cur, solutions)
        )
    elif not cur: # must flip
        ret = 1 + min_flips(s, ind + 1, 1, solutions)
    else: # must not flip
        ret = min_flips(s, ind + 1, 1, solutions)

    solutions[ind][prev] = ret
    return ret


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        # Time and Space Complexity: O(N)

        solutions = [[-1 for _ in range(2)] for _ in range(len(s))]
        return min_flips(s, 0, 0, solutions)
