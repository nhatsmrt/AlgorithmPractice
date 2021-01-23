class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        # Time Complexity: O(n log n)
        # Space Complexity: O(n)

        engineers = sorted(zip(efficiency, speed))
        MOD = 1000000007

        best_perf = -1
        cur_best_team = []
        cur_speed = 0

        for i in range(len(engineers) - 1, -1, -1):
            best_perf = max((engineers[i][1] + cur_speed) * engineers[i][0], best_perf)

            if len(cur_best_team) < k - 1:
                heapq.heappush(cur_best_team, engineers[i][1])
                cur_speed += engineers[i][1]
            elif k > 1 and engineers[i][1] > cur_best_team[0]:
                cur_speed += engineers[i][1] - cur_best_team[0]
                heapq.heapreplace(cur_best_team, engineers[i][1])

        return best_perf % MOD
