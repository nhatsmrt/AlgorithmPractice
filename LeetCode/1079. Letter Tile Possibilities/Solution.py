def count(cnter) -> int:
    ret = 1

    for char in cnter:
        if cnter[char] > 0:
            cnter[char] -= 1
            ret += count(cnter)
            cnter[char] += 1

    return ret

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        # Time Complexity: O(26^N)
        # Space Complexity: O(N)

        cnter = Counter(tiles)
        return count(cnter) - 1
