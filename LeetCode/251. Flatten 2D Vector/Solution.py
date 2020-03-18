class Vector2D:

    def __init__(self, v: List[List[int]]):
        self.row = 0
        self.col = 0
        self.data = v


    def next(self) -> int:
        ret = self.data[self.row][self.col]

        if self.col < len(self.data[self.row]) - 1:
            self.col += 1
        else:
            self.row += 1
            self.col = 0

        return ret


    def hasNext(self) -> bool:
        while self.row < len(self.data):
            if self.col < len(self.data[self.row]):
                return True
            else:
                self.row += 1
                self.col = 0

        return False



# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()
