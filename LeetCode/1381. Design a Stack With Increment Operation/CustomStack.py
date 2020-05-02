class CustomStack:

    def __init__(self, maxSize: int):
        # Time Complexity: O(1) per query
        # Extra space: O(1) per element

        self.maxSize = maxSize
        self.data = []
        self.inc = []


    def push(self, x: int) -> None:
        if len(self.data) < self.maxSize:
            self.data.append(x)
            self.inc.append(0)


    def pop(self) -> int:
        if len(self.data) == 0:
            return -1

        if len(self.data) > 1:
            self.inc[-2] += self.inc[-1] # propagate the update down

        return self.data.pop() + self.inc.pop()


    def increment(self, k: int, val: int) -> None:
        if len(self.data) > 0:
            k = min(len(self.data), k)
            k -= 1
            self.inc[k] += val




# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
