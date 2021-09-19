class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        # Time and Space Complexity: O(MN)

        ret = [[None for _ in range(len(box))] for _ in range(len(box[0]))]

        summaries = []

        for row in box:
            summary = []
            stone = 0
            space = 0

            for cell in row:
                if cell == "#":
                    stone += 1
                elif cell == ".":
                    space += 1
                else: # obstacle
                    summary.append((stone, space))
                    summary.append("*")

                    stone, space = 0, 0

            if stone or space:
                summary.append((stone, space))

            summaries.append(summary)

        for i, summary in enumerate(summaries):
            col_ind = len(summaries) - 1 - i
            cell_ind = 0

            for info in summary:
                if info == "*":
                    ret[cell_ind][col_ind] = "*"
                    cell_ind += 1
                else:
                    stone, space = info

                    for _ in range(space):
                        ret[cell_ind][col_ind] = "."
                        cell_ind += 1

                    for _ in range(stone):
                        ret[cell_ind][col_ind] = "#"
                        cell_ind += 1

        return ret
