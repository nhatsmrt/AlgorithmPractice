class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        # Time complexity: O(log p)
        # Space complexity: O(1)

        # Instead of simulating the ray bouncing of the side of the square
        # imagine we have a lattice, whose cells have the same size as the square
        # and the original square is the (0, 0), (0, 1), (1, 1), (1, 0) cell.
        # Then if the original tray hits the cell at the first lattice point (x, y)
        # then we can recover the corresponding hit angle in the original cell
        # by taking the top right corner
        # and then reflecting a square horizontally (x - 1) times
        # and vertically (y - 1) times.


        gcd = self.gcd(p, q)
        # (x, y) = (p / gcd(p, q), q / gcd(p, q)) is the first point on the lattice
        # that the ray memets.

        x = p // gcd
        y = q // gcd

        if (x - 1) % 2 == 0:
            if (y - 1) % 2 == 0:
                return 1
            else:
                return 0
        else:
            if (y - 1) % 2 == 0:
                return 2
            else:
                return 0


    def gcd(self, p, q):
        if p % q == 0:
            return q
        return self.gcd(q, p % q)
