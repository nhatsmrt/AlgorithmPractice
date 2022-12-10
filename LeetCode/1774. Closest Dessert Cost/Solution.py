def closest(topping_costs, index, num_chosen, cur, target, solutions):
    key = (index, num_chosen, cur)
    if key in solutions:
        return solutions[key]

    if index == len(topping_costs):
        return cur

    ret = closest(topping_costs, index + 1, 0, cur, target, solutions)
    if num_chosen < 2:
        cand = closest(topping_costs, index, num_chosen + 1, cur + topping_costs[index], target, solutions)
        if abs(target - cand) < abs(target - ret) or (abs(target - cand) == abs(target - ret) and ret > cand):
            ret = cand

    solutions[key] = ret
    return ret

class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        # Time and Space Complexity: O(N * W)
        # where W = max(abs(T - base_cost) for base_cost in base_costs)
        ret = -100000
        solutions = {}
        for base_cost in baseCosts:
            cand = closest(toppingCosts, 0, 0, base_cost, target, solutions)

            if abs(target - cand) < abs(target - ret) or (abs(target - cand) == abs(target - ret) and ret > cand):
                ret = cand

        return ret
