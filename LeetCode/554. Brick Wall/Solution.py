class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        # Time and Space Complexity: O(num_bricks)

        prefixes = list(map(list, map(itertools.accumulate, wall)))

        counter = Counter()
        for row in prefixes:
            for prefix_sum in row[:len(row) - 1]:
                counter[prefix_sum] += 1


        if counter:
            return len(wall) - max([counter[prefix_sum] for prefix_sum in counter])

        return len(wall)
