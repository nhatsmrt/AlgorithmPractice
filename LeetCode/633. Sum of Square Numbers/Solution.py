class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # Time Complexity: O(sqrt(c) log c)
        # Space Complexity: O(1)

        if c <= 1:
            return True

        if c % 4 == 3:
            return False

        if c % 4 == 0:
            return self.judgeSquareSum(c // 4)

        def is_square(x):
            sqrted = int(math.sqrt(x))
            return sqrted ** 2 == x

        for i in range(1, math.floor(math.sqrt(c)) + 1, 2):
            if is_square(c - i ** 2):
                return True

        return False
