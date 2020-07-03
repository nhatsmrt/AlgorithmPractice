class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        # Time and Space Complexity: min(N, 2^len(cells))

        # cell[0][t] = cell[-1][t] = 0, for all t
        # cell[i][t] = ~(cell[i][t - 1], cell[i][t])
        code = self.get_code(cells)
        code_to_t = {code: 0}
        t_to_code = [code]


        for i in range(N):
            code = self.advance(code)

            if code in code_to_t: # repeat itself
                t = code_to_t[code]
                return self.get_cell(t_to_code[t + (N - t) % (len(t_to_code) - t)])
            else:
                code_to_t[code] = len(t_to_code)
                t_to_code.append(code)

        return self.get_cell(code)

    def get_code(self, cells: List[int]) -> int:
        return int(''.join(map(str, cells)), 2)

    def get_cell(self, code: int) -> List[int]:
        ret = []

        while code > 0:
            ret.append(code & 1)
            code >>= 1

        if len(ret) < 8:
            ret.extend([0] * (8 - len(ret)))

        return ret[::-1]

    def advance(self, code: int) -> int:
        return ((((code >> 2) ^ code) ^ (255)) << 1) & 127
