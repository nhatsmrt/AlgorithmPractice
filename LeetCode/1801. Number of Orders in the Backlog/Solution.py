class MultiIxPQ:
    def __init__(self):
        self.data = []
        self.index = {}

    def push(self, price, amount):
        if price in self.index:
            ind = self.index[price]
            self.data[ind] = (price, self.data[ind][1] + amount)
        else:
            self.data.append((price, amount))
            self.index[price] = len(self.data) - 1
            self.sift_up(len(self.data) - 1)



    def pop(self):
        self.swap(0, len(self.data) - 1)
        ret = self.data.pop()
        self.index.pop(ret[0])

        if self.data:
            self.sift_down(0)

        return ret

    def sift_up(self, i):
        par = (i - 1) // 2

        if par >= 0 and self.data[par][0] > self.data[i][0]:
            self.swap(par, i)
            self.sift_up(par)

    def sift_down(self, i):
        child = None
        left = i * 2 + 1
        right = i * 2 + 2

        if right < len(self.data) and self.data[right][0] < self.data[left][0]:
            child = right
        elif left < len(self.data):
            child = left

        if child is not None and self.data[child][0] < self.data[i][0]:
            self.swap(i, child)
            self.sift_down(child)

    def swap(self, i1, i2):
        data1, data2 = self.data[i1], self.data[i2]
        self.data[i2] = data1
        self.data[i1] = data2

        self.index[data1[0]] = i2
        self.index[data2[0]] = i1


    def __getitem__(self, i: int):
        return self.data[i]

    def __len__(self): return len(self.data)

    def __str__(self): return str(self.data)



class Solution:
    _MOD = 1000000007
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        # Time Complexity: O(|batch| log |batch|)
        # Each iteration of the while loop, there's 2 cases:
        # a) Either at least one sell or one buy is resolved
        # b) one sell/buy is added to the backlog
        # There can be at most |batch| addition to backlog operation
        # and O(|batch|) resolution

        # Space Complexity: O(|batch|)

        sells = MultiIxPQ()
        buys = MultiIxPQ()

        for price, amount, order_type in orders:
            while amount:
                if order_type: # sell
                    if buys and -buys[0][0] >= price:
                        buy_price, buy_amount = buys.pop()

                        new_buy_amount = max(0, buy_amount - amount)
                        amount = max(0, amount - buy_amount)

                        if new_buy_amount:
                            buys.push(buy_price, new_buy_amount)
                    else:
                        sells.push(price, amount)
                        break
                else: # buy
                    if sells and sells[0][0] <= price:
                        sell_price, sell_amount = sells.pop()

                        new_sell_amount = max(0, sell_amount - amount)
                        amount = max(0, amount - sell_amount)

                        if new_sell_amount:
                            sells.push(sell_price, new_sell_amount)
                    else:
                        buys.push(-price, amount)
                        break

        ret = 0
        for data in (sells.data, buys.data):
            for _, amount in data:
                ret += amount
                ret %= self._MOD

        return ret
