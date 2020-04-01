from collections import Counter

class FreqStack:

    def __init__(self):
        self.data = []
        self.cnter = Counter()


    def push(self, x: int) -> None:
        cnt = self.cnter[x]

        if cnt == len(self.data):
            self.data.append([])

        self.data[cnt].append(x)
        self.cnter[x] = cnt + 1


    def pop(self) -> int:
        while len(self.data[-1]) == 0:
            self.data.pop()

        ret = self.data[-1].pop()
        self.cnter[ret] -= 1

        return ret



# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
