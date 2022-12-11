MOD = 10 ** 9 + 7


def count(s: str, i: int, k: int, solutions) -> int:
    if i == len(s):
        return 1

    if s[i] == "0":
        return 0 # no leading zeroes

    if solutions[i] is not None:
        return solutions[i]

    ret = 0
    cur = int(s[i])
    end = i

    while cur <= k and end < len(s):
        ret += count(s, end + 1, k, solutions)
        ret %= MOD

        end += 1
        if end < len(s):
            cur = cur * 10 + int(s[end])

    solutions[i] = ret
    return ret


class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        # Time Complexity: O(|s| * log_10(k))
        # Space Complexity: O(|s|)
        return count(s, 0, k, [None] * len(s))
