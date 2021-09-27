class Solution:
    def decodeString(self, s: str) -> str:
        stack = [[]]
        self.decode(s, 0, stack)
        return "".join(stack[0])

    def decode(self, s: str, i: int, stack: List[List[str]]) -> int:
        if i == len(s):
            return i # done

        if s[i].isdigit():
            # handle repeats
            end = i

            while end + 1 < len(s) and s[end + 1].isdigit():
                end += 1

            num_repeats = int(s[i:end + 1])
            stack.append([])
            next_index = self.decode(s, end + 2, stack)

            repeated = stack.pop()
            for _ in range(num_repeats):
                stack[-1].extend(repeated)

            return self.decode(s, next_index, stack)

        elif s[i] == "]":
            return i + 1
        else:
            stack[-1].append(s[i])
            return self.decode(s, i + 1, stack)
