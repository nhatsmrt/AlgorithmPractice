MOD = 10 ** 9 + 7

def count_num_ways(n, k, target, dp):
    if (n, target) in dp:
        return dp[(n, target)]

    # base case: no more turns or reach target
    if n == 0 or target == 0:
        if n == 0 and target == 0:
            return 1
        else:
            # reach target prematurely
            # or out of turns without reaching target
            return 0

    ret = 0
    for result in range(1, min(k + 1, target + 1)):
        ret += count_num_ways(n - 1, k, target - result, dp)
        ret %= MOD


    dp[(n, target)] = ret
    return ret


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        # Time Complexity: O(NKT)
        # Space Complexity: O(NT)

        return count_num_ways(n, k, target, {})
