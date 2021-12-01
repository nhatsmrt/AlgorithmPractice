class Solution:
    def numWays(self, s: str) -> int:
        # Time and Space Complexity: O(N)
        prefix = list(accumulate(map(int, s)))
        cnter = Counter(prefix)
        total = prefix[-1]

        if total % 3:
            return 0

        if not total:
            return ((len(s) - 2) * (len(s) - 1) // 2) % (1000000007)

        first_third = total // 3
        second_third = total // 3 * 2

        return (cnter[first_third] * cnter[second_third]) % (1000000007)
