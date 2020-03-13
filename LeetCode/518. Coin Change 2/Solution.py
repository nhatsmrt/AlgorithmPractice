class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Time and Space Complexity: O(amount x N)

        self.cache = [{} for i in range(len(coins))]
        return self.dp(0, amount, coins)

    def dp(self, ind: int, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1

        if ind == len(coins):
            return 0

        if amount in self.cache[ind]:
            return self.cache[ind][amount]

        ret = self.dp(ind + 1, amount, coins)
        if amount >= coins[ind]:
            ret += self.dp(ind, amount - coins[ind], coins)

        self.cache[ind][amount] = ret
        return ret
