class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.counter = 0
        self.n, self.discount, self.products = n, discount, products
        self.prices = {}

        for product_id, price in zip(products, prices):
            self.prices[product_id] = price

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.counter += 1
        self.counter %= self.n

        cost_per_item = map(lambda p: self.prices[p], product)
        total_bill = sum(map(lambda x: x[0] * x[1], zip(cost_per_item, amount)))

        if not self.counter:
            total_bill = total_bill * (100 - self.discount) / 100

        return total_bill

# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)
