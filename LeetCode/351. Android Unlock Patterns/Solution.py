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
        used = ["0" for i in range(10)]
        for i in range(1, 10):
            used[i - 1] = "1"
            used_digs = set([i])
            ret += self.count_solutions(i, "".join(used), used_digs, m, n)
            used[i - 1] = "0"

        return ret


    def count_solutions(self, cur_pos: int, used_mask: str, used_digs: set, m: int, n: int) -> int:
        if (cur_pos, used_mask) in self.dp:
            return self.dp[(cur_pos, used_mask)]
        ret = 0

        if len(used_digs) >= m:
            ret += 1

        if len(used_digs) == n:
            return ret

        for i in range(1, 10):
            if used_mask[i - 1] == "0":
                if (cur_pos, i) not in self.passed_through or used_mask[self.passed_through[(cur_pos, i)] - 1] == "1":
                    new_state = list(iter(used_mask))
                    new_state[i - 1] = "1"
                    used_digs.add(i)
                    ret += self.count_solutions(i, "".join(new_state), used_digs, m, n)
                    used_digs.remove(i)

        self.dp[(cur_pos, used_mask)] = ret
        return ret
