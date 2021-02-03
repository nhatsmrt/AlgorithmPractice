class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if not numRows:
            return []

        ret = [[1]]

        for _ in range(1, numRows):
            new_row = [1]

            for i in range(1, len(ret[-1])):
                new_row.append(ret[-1][i] + ret[-1][i - 1])

            new_row.append(1)
            ret.append(new_row)

        return ret
