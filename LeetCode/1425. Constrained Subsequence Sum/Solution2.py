class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        # Time and Space Complexity: O(N)

        # Let dp[i] be the max constrained subseq sum starting from nums[i]
        # dp[i] = nums[i] + max(0, dp[i + 1], ..., dp[i + k - 1])
        # answer = max_i dp[i]

        window = deque()
        window_size = 0
        ret = -100000000000

        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]

            if window_size == 0:  # base case
                solution = num
            else:
                solution = num + max(0, window[-1][0])

            if window_size == k:
                last, last_cnt = window.pop()
                if last_cnt > 1:
                    window.append((last, last_cnt - 1))
            else:
                window_size += 1

            # insert solution to window:
            cnt = 1
            while window and window[0][0] <= solution:
                cnt += window.popleft()[1]

            window.appendleft((solution, cnt))


            ret = max(ret, solution)

        return ret
    
