class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        # Time and Space Complexity: O(sqrt(N))

        factors = []

        for i in range(1, int(math.sqrt(n)) + 1):
            if n % i == 0:
                k -= 1
                factors.append(i)

                if not k:
                    return i

        if factors[-1] ** 2 < n:
            if k <= len(factors):
                return n // factors[-k]
        else:
            if k < len(factors):
                return n // factors[-k - 1]

        return -1
                    
