class Solution:
    _MOD = 1000000007
    def countPairs(self, deliciousness: List[int]) -> int:
        # Time Complexity: O(N log MAX_VAL)
        # Space Complexity: O(N)

        condensed = Counter()

        for del_value in deliciousness:
            condensed[del_value] += 1

        target = 1
        limit = max(deliciousness) * 2
        ret = 0

        while target <= limit:
            for del_value in condensed:
                if del_value * 2 < target:
                    ret += condensed[del_value] * condensed[target - del_value]
                    ret %= self._MOD
                elif del_value * 2 == target:
                    ret += condensed[del_value] * (condensed[del_value] - 1) // 2
                    ret %= self._MOD

            target *= 2

        return ret
