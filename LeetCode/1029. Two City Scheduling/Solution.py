class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda cost: -abs(cost[0] - cost[1]))

        ret = 0
        assigned = [0, 0]

        for cost in costs:
            argmin = self.argmin(cost)

            if assigned[argmin] < len(costs) // 2:
                assigned[argmin] += 1
                ret += cost[argmin]
            else:
                assigned[1 - argmin] += 1
                ret += cost[1 - argmin]

        return ret

    def argmin(self, cost: List[int]) -> int:
        if cost[0] < cost[1]:
            return 0

        return 1
