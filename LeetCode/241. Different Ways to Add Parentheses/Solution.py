from collections import deque


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        operators = []

        for i, char in enumerate(expression):
            if not char.isdigit():
                operators.append(i)

        def build(expr_start, expr_end, operators_start, operators_end, solutions) -> List[int]:
            key = (expr_start, expr_end)

            if key in solutions:
                return solutions[key]

            if operators_start + 1 >= operators_end:
                ret = [int(eval(expression[expr_start:expr_end]))]
            else:
                ret = []

                for operators_i in range(operators_start, operators_end):
                    operator_expr_i = operators[operators_i]

                    for first in build(expr_start, operator_expr_i, operators_start, operators_i, solutions):
                        for second in build(operator_expr_i + 1, expr_end, operators_i + 1, operators_end, solutions):
                            chosen_operator = expression[operator_expr_i]
                            ret.append(eval(f"{first}{chosen_operator}{second}"))



            solutions[key] = ret
            return ret


        return build(0, len(expression), 0, len(operators), {})
