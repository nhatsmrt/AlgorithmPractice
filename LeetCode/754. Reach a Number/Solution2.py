class Solution:
    def reachNumber(self, target: int) -> int:
        # Time and Space Complexity: O(1)

        if not target:
            return 0

        if target < 0:
            return self.reachNumber(-target)

        # n * (n + 1) // 2 - target = 2 * x
        # n * (n + 1) = 2 * target + 4 * x
        # n^2 + n >= 2 * target
        # (n + 0.5)^2 >= 2 * target + 0.25
        # n >= ceil(-0.5 + sqrt(2 * target + 0.25))

        ret = math.ceil(-0.5 + math.sqrt(2 * target + 0.25))

        while (ret * (ret + 1) - 2 * target) % 4:
            ret += 1

        return ret
