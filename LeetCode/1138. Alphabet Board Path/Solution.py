class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        # Time and Space Complexity: O(|target|)

        index = {}

        for i in range(26):
            char = chr(ord('a') + i)

            row = i // 5
            col = i % 5
            index[char] = (row, col)

        cur = (0, 0)

        ret = []
        for char in target:
            next_pos = index[char]
            dx, dy = next_pos[0] - cur[0], next_pos[1] - cur[1]

            if next_pos == (5, 0):
                for _ in range(abs(dy)):
                    if dy < 0:
                        ret.append("L")
                    else:
                        ret.append("R")

                for _ in range(abs(dx)):
                    if dx < 0:
                        ret.append("U")
                    else:
                        ret.append("D")
            else:
                for _ in range(abs(dx)):
                    if dx < 0:
                        ret.append("U")
                    else:
                        ret.append("D")

                for _ in range(abs(dy)):
                    if dy < 0:
                        ret.append("L")
                    else:
                        ret.append("R")



            ret.append("!")
            cur = next_pos

        return "".join(ret)
