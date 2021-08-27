class Solution:
    def divisorGame(self, n: int) -> bool:
        # The game concludes when n == 1

        # If any player gets an even number, they win (by subtracting 1)
        # The opponent, since they can't subtract an even number, must subtract an odd number
        # giving the player back an even number

        return not n % 2
