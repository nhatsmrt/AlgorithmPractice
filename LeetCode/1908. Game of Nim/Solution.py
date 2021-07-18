class Solution:
    def nimGame(self, piles: List[int]) -> bool:
        # Time Complexity: O(N)
        # Space Complexity: O(1)

        # Theorem (Sprague-Gundy): Alice wins i.f.f XOR(piles) != 0
        # Strategy: pick the number of stones that would bring this to 0

        return reduce(lambda x, y: x ^ y, piles) != 0
        
