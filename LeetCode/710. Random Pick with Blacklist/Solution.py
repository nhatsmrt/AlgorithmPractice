import random as random

class Solution:

    def __init__(self, N: int, blacklist: List[int]):
        # Time Complexity: <O(B log B), O(log B)>
        # Space Complexity: O(1)
        blacklist.sort()
        self.blacklist = blacklist
        self.N = N


    def pick(self) -> int:
        val = random.randint(0, self.N - len(self.blacklist) - 1)

        if len(self.blacklist) == 0 or val < self.blacklist[0]:
            return val

        val -= self.blacklist[0] - 1
        low = 0
        high = len(self.blacklist)

        while low + 1 < high:
            mid = low + (high - low) // 2
            gaps = self.blacklist[mid] - self.blacklist[low] + low - mid

            if gaps >= val:
                high = mid
            else:
                low = mid
                val -= gaps

        return self.blacklist[low] + val



# Your Solution object will be instantiated and called as such:
# obj = Solution(N, blacklist)
# param_1 = obj.pick()
