class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # Time Complexity: O(N)
        # Space Complexity: O(1)

        # Let f(i) be the max number of pots that can be placed in bed[i:]
        # Observation 1: f(i) >= f(i + 1)
        # Observation 2: if we place in bed i, then max placed pots = f(i + 2) + 1
        # if we don't, then max placed pots = f(i + 3) + 1
        # In other words, if we can place a pot at bed i (given all the previous pots)
        # it's always as least as good placing a pot there as not.
        # In other words, we can greedily place the pots


        ret = 0
        for i in range(len(flowerbed)):
            if not flowerbed[i] and (i == 0 or not flowerbed[i - 1]) and (i == len(flowerbed) - 1 or not flowerbed[i + 1]):
                ret += 1
                flowerbed[i] = 1

        return n <= ret
