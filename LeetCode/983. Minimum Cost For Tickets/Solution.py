class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # Time Complexity: O(N)
        # Space Complexity: O(N)

        self.dp = [-1] * len(days)
        self.durations = [1, 7, 30]

        return self.find_min(days, costs, 0)

    def find_min(self, days: List[int], costs: List[int], day: int) -> int:
        if day >= len(days):
            return 0
        elif self.dp[day] >= 0:
            return self.dp[day]
        else:
            candidates = []

            for duration, cost in zip(self.durations, costs):
                new_day = day + 1
                end = days[day] + duration

                while new_day < len(days) and days[new_day] < end:
                    new_day += 1

                candidates.append(cost + self.find_min(days, costs, new_day))

            self.dp[day] = min(candidates)
            return self.dp[day]
            
