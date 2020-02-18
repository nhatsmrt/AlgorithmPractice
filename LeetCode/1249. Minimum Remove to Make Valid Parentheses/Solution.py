class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        num_open = 0
        ret_arr = []

        for char in s:
            if char == '(':
                stack.append(char)
                num_open += 1
            elif char == ')':
                if num_open > 0:
                    stack.append(char)
                    num_open -= 1
            else:
                stack.append(char)

        stack2 = []
        num_close = 0
        while len(stack) > 0:
            char = stack.pop()
            if char == ')':
                num_close += 1
                stack2.append(char)
            elif char == '(':
                if num_close > 0:
                    num_close -= 1
                    stack2.append(char)
            else:
                stack2.append(char)

        return ''.join(stack2[::-1])
        
