class ProductOfNumbers:

    def __init__(self):
        self.prefix = [1]


    def add(self, num: int) -> None:
        if num == 0:
            self.prefix = [1]
        else:
            self.prefix.append(self.prefix[-1] * num)


    def getProduct(self, k: int) -> int:
        if k > len(self.prefix) - 1:
            return 0
        return self.prefix[-1] // self.prefix[-k - 1]



# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
