MOD = 10 ** 9 + 7


@cache
def count(dist, remain):
    if remain == 0:
        return 1 if dist == 0 else 0

    if dist > remain:
        return 0

    return (count(dist - 1, remain - 1) + count(dist + 1, remain - 1)) % MOD


class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        # Time and Space Complexity: O(k^2)
        return count(endPos - startPos, k)
