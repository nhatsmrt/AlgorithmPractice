class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        pairs = [
            (1, 3),
            (4, 6),
            (7, 9),
            (1, 7),
            (2, 8),
            (3, 9),
            (1, 9),
            (3, 7)
        ]
        self.passed_through = {}
        for pair in pairs:
            passed_through = (pair[0] + pair[1]) // 2
            self.passed_through[pair] = passed_through
            self.passed_through[(pair[1], pair[0])] = passed_through

        self.dp = {}
        ret = 0
        for i in range(1, 10):
            used_mask = 1 << (9 - i)
            used_digs = set([i])
            ret += self.count_solutions(i, used_mask, used_digs, m, n)

        return ret


    def count_solutions(self, cur_pos: int, used_mask: int, used_digs: set, m: int, n: int) -> int:
        if (cur_pos, used_mask) in self.dp:
            return self.dp[(cur_pos, used_mask)]
        ret = 0

        if len(used_digs) >= m:
            ret += 1

        if len(used_digs) == n:
            return ret

        for i in range(1, 10):
            dig_mask = 1 << (9 - i)
            if not (used_mask & dig_mask):
                if (cur_pos, i) not in self.passed_through or (used_mask & (1 << (9 - self.passed_through[(cur_pos, i)]))):
                    new_state = used_mask | dig_mask
                    used_digs.add(i)
                    ret += self.count_solutions(i, new_state, used_digs, m, n)
                    used_digs.remove(i)

        self.dp[(cur_pos, used_mask)] = ret
        return ret
                
