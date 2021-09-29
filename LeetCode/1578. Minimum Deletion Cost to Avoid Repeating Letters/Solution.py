class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        # Time Complexity: O(N)
        # Space Complexity: O(1)

        start = 0
        end = 0

        total_cost = cost[0]
        max_cost = cost[0]
        ret = 0

        while start < len(s):
            if end + 1 < len(s) and s[end + 1] == s[start]:
                end += 1
                total_cost += cost[end]
                max_cost = max(max_cost, cost[end])
            else:
                ret += total_cost - max_cost

                end += 1
                start = end

                if start < len(s):
                    total_cost = cost[start]
                    max_cost = cost[start]

        return ret
