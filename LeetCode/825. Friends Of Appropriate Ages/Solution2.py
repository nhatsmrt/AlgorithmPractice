class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        # Time and Space Complexity: O(N)
        # Space Complexity: O(1)

        ages_cnter = [0] * 121
        for age in ages:
            ages_cnter[age] += 1

        cum_dist = list(accumulate(ages_cnter))

        ret = 0
        for age_y in range(1, 121):
            # age_x >= age_y > 0.5 * age[x] + 7
            # 2 * (age_y - 7) > age_x >= age_y
            lower_bound = age_y
            upper_bound = min(2 * (age_y - 7), 121)

            # range of age of x: [lower_bound, upper_bound)
            if upper_bound > lower_bound:
                ret += ages_cnter[age_y] * (cum_dist[upper_bound - 1] - cum_dist[lower_bound - 1] - 1)

        return ret
