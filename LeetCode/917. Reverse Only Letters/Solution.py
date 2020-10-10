def is_letter(char):
    return (ord('a') <= ord(char) and ord(char) <= ord("z")) or  (ord('A') <= ord(char) and ord(char) <= ord("Z"))

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        letter_stack = []
        symbol_queue = collections.deque()

        for i, char in enumerate(S):
            if is_letter(char):
                letter_stack.append(char)
            else:
                symbol_queue.append((i, char))

        ret = []
        while len(symbol_queue) and letter_stack:
            i, char = symbol_queue[0]
            if len(ret) == i:
                symbol_queue.popleft()
                ret.append(char)
            else:
                ret.append(letter_stack.pop())


        while len(symbol_queue):
            ret.append(symbol_queue.popleft()[1])

        while letter_stack:
            ret.append(letter_stack.pop())

        return "".join(ret)
