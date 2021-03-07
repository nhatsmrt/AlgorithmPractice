class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        # Time Complexity: O(log(sum(weights)) * N)
        # Space Complexity: O(1)

        low = max(weights)
        high = sum(weights)

        while low < high:
            candidate = low + (high - low) // 2

            if self.num_days(weights, candidate) > D:
                low = candidate + 1
            else:
                high = candidate

        return low


    def num_days(self, weights: List[int], capacity: int) -> int:
        ret = 0
        cur = 0

        for weight in weights:
            if cur + weight <= capacity:
                cur += weight
            else:
                ret += 1
                cur = weight

        return ret + 1
