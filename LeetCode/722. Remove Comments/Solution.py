class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        # Time and Space Complexity: O(number of characters)

        ret = []
        lines_to_consider = list(zip(reversed(source), [0] * len(source)))

        def check(first, second) -> bool:
            return first >= 0 and (second < 0 or first <= second)

        in_block_cmt = False
        pre_block = ""

        while lines_to_consider:
            line, check_from = lines_to_consider.pop()

            double_slash = line[check_from:].find("//")
            start_block = line[check_from:].find("/*")

            if not in_block_cmt and check(double_slash, start_block):
                # found a double slash comment
                ret.append(line[:double_slash + check_from])
            elif not in_block_cmt and check(start_block, double_slash):
                # found begin of block cmt
                in_block_cmt = True
                pre_block = line[:start_block + check_from]
                remainder = line[start_block + check_from + 2:]

                end_block = remainder.find("*/")

                if end_block >= 0:
                    lines_to_consider.append((pre_block + remainder[end_block + 2:], len(pre_block)))
                    in_block_cmt = False
                    pre_block = ""

            elif in_block_cmt:
                end_block = line[check_from:].find("*/")

                if end_block >= 0:
                    lines_to_consider.append((pre_block + line[end_block + 2:], len(pre_block)))
                    in_block_cmt = False
                    pre_block = ""
            else:
                ret.append(line)

        return list(filter(lambda line: line, ret)) # filter empty lines
