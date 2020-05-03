class Solution:
    def minmaxGasDist(self, stations: List[int], K: int) -> float:
        # Time Complexity: O(N log (max_val / epsilon))
        # Space Complexity: O(1)

        eps = 1e-6

        low = 0.0
        high = max(stations[i + 1] - stations[i] for i in range(len(stations) - 1))

        while low + eps < high:
            mid = low + (high - low) / 2
            if self.isFeasible(stations, mid, K):
                high = mid
            else:
                low = mid

        return high

    def isFeasible(self, stations: List[int], target: float, K: int) -> bool:
        num_added = 0

        for i in range(len(stations) - 1):
            dist = stations[i + 1] - stations[i]

            if dist > target:
                candidate = int((stations[i + 1] - stations[i]) // target)
                num_added += candidate

        return num_added <= K

        
