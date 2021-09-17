class Solution:
    def divisorGame(self, n: int) -> bool:
        # Time and Space Complexity: O(N (1 + 1 / 2 + ... + 1 /N)) = O(N log N)
        divisors = {}

        for divisor in range(1, n + 1):
            i = 2

            while divisor * i <= n:
                num = divisor * i

                if num not in divisors:
                    divisors[num] = set()

                divisors[num].add(divisor)
                i += 1

        self.divisors = divisors
        self.dp = {}

        return self.play(n)

    def play(self, n):
        if n in self.dp:
            return self.dp[n]

        if n == 1:
            return False

        ret = False
        for divisor in self.divisors[n]:
            ret = ret or not (self.play(n - divisor))

        self.dp[n] = ret
        return ret
