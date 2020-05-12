class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        # Time and Space Complexity: O(MN)

        self.dp = {}
        return self.travel(dungeon, 0, 0)

    def travel(self, dungeon: List[List[int]], i: int, j: int) -> int:
        if (i, j) in self.dp:
            return self.dp[(i, j)]

        if i == len(dungeon) - 1 and j == len(dungeon[0]) - 1:
            self.dp[(i, j)] = max(1, 1 - dungeon[i][j])
        else:
            candidates = []

            if i < len(dungeon) - 1:
                candidates.append(self.travel(dungeon, i + 1, j))

            if j < len(dungeon[0]) - 1:
                candidates.append(self.travel(dungeon, i, j + 1))

            self.dp[(i, j)] = max(1, min(candidates) - dungeon[i][j])

        return self.dp[(i, j)]
        
