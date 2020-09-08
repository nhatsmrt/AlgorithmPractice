class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        # Time Complexity: O(N 4^N)
        # Space Complexity: O(N)

        if not num:
            return []

        self.operators = ["+", "-", "*"]
        ret = []

        self.build(num, 0, -1, [], target, ret)
        return ret

    def build(self, num: str, pos: int, last_operator: int, sol: List[str], target: int, ret: List[str]):
        if pos == len(num):
            sol_str = "".join(sol)

            if eval(sol_str) == target:
                ret.append(sol_str)
        else:
            if last_operator == len(sol) - 1 or sol[last_operator + 1] != "0":
                sol.append(num[pos])
                self.build(num, pos + 1, last_operator, sol, target, ret)
                sol.pop()

            if len(sol) and sol[-1] not in self.operators:
                for operator in self.operators:
                    sol.append(operator)
                    self.build(num, pos, len(sol) - 1, sol, target, ret)
                    sol.pop()
