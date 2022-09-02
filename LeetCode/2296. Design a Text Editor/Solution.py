class TextEditor:

    def __init__(self):
        self.before, self.after = [], []

    def addText(self, text: str) -> None:
        self.before.extend(text)


    def deleteText(self, k: int) -> int:
        ret = 0

        while k and self.before:
            self.before.pop()
            k -= 1
            ret += 1

        return ret


    def cursorLeft(self, k: int) -> str:
        while k and self.before:
            self.after.append(self.before.pop())
            k -= 1

        return self._return()

    def cursorRight(self, k: int) -> str:
        while k and self.after:
            self.before.append(self.after.pop())
            k -= 1

        return self._return()

    def _return(self):
        ret_len = min(10, len(self.before))
        return "".join(self.before[len(self.before) - ret_len:])



# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)
