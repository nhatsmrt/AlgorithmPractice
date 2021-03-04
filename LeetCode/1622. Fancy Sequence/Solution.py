from functools import cache


@cache
def inverse(num):
    # Time Complexity: O(log MOD) = O(W)
    MOD = 1000000007

    # By Fermat's theorem:
    # num^{MOD - 1} == 1 (mod MOD)
    # so num^{MOD - 2} == num^{-1} (mod MOD)

    # num^{1001} = num^{1 + 1000} = num^1 * num^{1000}

    power = MOD - 2  # need to find num^power mod MOD
    cur = num

    ret = 1
    while power > 0:
        if (power & 1):
            ret *= cur
            ret %= MOD

        cur *= cur
        cur %= MOD
        power >>= 1

    return ret

# Space Complexity: O(Q + MOD)
class Fancy:

    def __init__(self):
        self.data = []
        self.multiplier = 1
        self.adder = 0
        self.MOD = 1000000007


    def append(self, val: int) -> None:
        # Time Complexity: O(1)
        self.data.append(((val - self.adder), self.multiplier))


    def addAll(self, inc: int) -> None:
        # Time Complexity: O(1)
        self.adder += inc

    def multAll(self, m: int) -> None:
        # Time Complexity: O(1)
        self.multiplier *= m
        self.multiplier %= self.MOD

        self.adder *= m
        self.adder %= self.MOD

    def getIndex(self, idx: int) -> int:
        # Time Complexity: O(log MOD) = O(W)
        # where W is the number digit of 1e9 + 7
        if idx >= len(self.data):
            return -1

        numerator, denominator = self.data[idx]
        inverse_denominator = inverse(denominator)
        ret = (numerator * self.multiplier % self.MOD * inverse_denominator % self.MOD + self.adder) % self.MOD
        return ret







# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)
