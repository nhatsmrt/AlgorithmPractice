from itertools import product


class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        # Grammar:
        # S -> U
        # U -> char U | L U | empty (union)
        # L -> { HU } (list)
        # H -> empty | U,H (heads)

        return sorted(self.parse_concat(expression, 0)[0])

    def parse_concat(self, expression: str, i: int):
        subresults = []
        cur = i

        while cur < len(expression):
            if expression[cur] == "{":
                subres, end = self.parse_list(expression, cur)
                cur = end
                subresults.append(subres)
            elif expression[cur].isalnum():
                subresults.append([expression[cur]])
                cur += 1
            elif expression[cur] in ",}":
                break

        ret = set()
        for options in product(*subresults):
            ret.add("".join(options))


        return ret, cur

    def parse_list(self, expression: str, i: int):
        cur = i + 1
        ret = set()

        while cur < len(expression):
            if expression[cur] == ",":  # delimiter
                cur += 1
            elif expression[cur] == "}": # finish
                cur += 1
                break
            else:
                subresult, end = self.parse_concat(expression, cur)
                ret.update(subresult)
                cur = end

        return ret, cur
