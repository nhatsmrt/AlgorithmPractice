class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        # 4x + 2y = tomatoSlices
        # x + y = cheeseSlices
        # Time and Space Complexity: O(1)

        if tomatoSlices % 2 != 0 or tomatoSlices - 2 * cheeseSlices < 0:
            return []

        jumbo = (tomatoSlices - 2 * cheeseSlices) // 2
        small = cheeseSlices - jumbo

        if small < 0:
            return []

        return [jumbo, small]
        
