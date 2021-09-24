class Solution:
    def minimumDistance(self, word: str) -> int:
        # Time and Space Complexity: O(N) (big constant)

        positions = {}
        available_positions = []

        for i in range(26):
            char = chr(ord('A') + i)
            row = i // 6
            col = i % 6

            positions[char] = (row, col)
            available_positions.append((row, col))

        word_pos = list(map(lambda char: positions[char], word))
        dp = {}

        def dist(pos1, pos2):
            return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

        def solve(pos1, pos2, ind):
            if ind == len(word):
                return 0

            if (pos1, pos2, ind) in dp:
                return dp[(pos1, pos2, ind)]

            new_pos = word_pos[ind]
            ret = min(
                dist(pos1, new_pos) + solve(new_pos, pos2, ind + 1),
                dist(pos2, new_pos) + solve(pos1, new_pos, ind + 1)
            )

            dp[(pos1, pos2, ind)] = ret
            return ret

        ret = None
        for pos1 in available_positions:
            for pos2 in available_positions:
                total_dist = solve(pos1, pos2, 0)

                if ret is None or ret > total_dist:
                    ret = total_dist

        return ret
