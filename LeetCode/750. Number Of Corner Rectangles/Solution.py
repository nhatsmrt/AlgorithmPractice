class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        # Time Complexity: O(R * C^2)
        # Space Complexity: O(C^2)

        counter = Counter()  # count[(i, j)] = # rows with row[i] = row[j] = 1

        for row in grid:
            for i, val in enumerate(row):
                if val:
                    for j in range(i + 1, len(row)):
                        if row[j]:
                            counter[(i, j)] += 1

        return sum([counter[key] * (counter[key] - 1) // 2 for key in counter])
