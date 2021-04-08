class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # Time and Space Complexity: O(N log W)
        # where W is the max price

        # Lagrangian relaxation (Alien) trick
        # Let f(k) = max profit using exactly k transactions
        # then f is a concave function, i.e adding transaction give diminishing returns:
        # f(k) - f(k - 1) >= f(k + 1) - f(k)

        prices = self.compact(prices)

        if len(prices) < 2:
            return 0

        low = 0
        high = max(prices)

        ret = 0

        while low <= high:
            mid = low + (high - low) // 2
            profit, min_transaction = self.maxProfitWithPenalty(prices, mid, True)
            _, max_transaction = self.maxProfitWithPenalty(prices, mid, False)

            if min_transaction > k:
                low = mid + 1
            else:
                high = mid - 1
                ret = max(ret, profit + min(k, max_transaction) * mid)

        return ret

    def compact(self, prices: List[int]) -> List[int]:
        # only consider peaks and valleys in list of prices
        ret = []
        desc = False
        cur = 0

        while cur < len(prices):
            if desc:
                if cur + 1 == len(prices) or prices[cur] > prices[cur + 1]:
                    ret.append(prices[cur])
                    desc = False
            else:
                if cur + 1 == len(prices) or prices[cur] < prices[cur + 1]:
                    ret.append(prices[cur])
                    desc = True

            cur += 1

        return ret


    def maxProfitWithPenalty(self, prices: List[int], penalty: int, low_transact: bool):
        self.dp = {}
        return self.solve(prices, 0, 0, penalty, low_transact)

    def solve(self, prices: List[int], i: int, bought: bool, penalty: int, low_transact: bool) -> int:
        if i == len(prices):
            return 0, 0

        if (i, bought) in self.dp:
            return self.dp[(i, bought)]

        inaction_prof, inaction_transact = self.solve(prices, i + 1, bought, penalty, low_transact)
        action_prof, action_transact = self.solve(prices, i + 1, 1 - bought, penalty, low_transact)

        if bought:
            action_prof += prices[i]
        else:
            action_prof -= prices[i] + penalty
            action_transact += 1

        self.dp[(i, bought)] = max(
            [(inaction_prof, inaction_transact), (action_prof, action_transact)],
            key=lambda pair: (pair[0], -pair[1] if low_transact else pair[1])
        )

        return self.dp[(i, bought)]
