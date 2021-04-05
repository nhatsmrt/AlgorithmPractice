class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        # Time Complexity: O(N log N + Q)
        # Space Complexity: O(N)

        MOD = 1000000007
        # diff_arr[0] = num_request[0]
        # diff_arr[i] = num_request[i] - num_request[i - 1]
        diff_arr = [0] * len(nums)

        for req in requests:
            diff_arr[req[0]] += 1

            if req[1] + 1 < len(diff_arr):
                diff_arr[req[1] + 1] -= 1

        num_requests = [diff_arr[0]]
        for i in range(1, len(diff_arr)):
            num_requests.append(num_requests[-1] + diff_arr[i])

        # Greedy Strategy: assign the biggest values to slot with max request, etc.
        # Proof: by Rearrangement Inequality
        ret = 0
        for num_req, value in zip(sorted(num_requests), sorted(nums)):
            ret += num_req * value
            ret %= MOD

        return ret
