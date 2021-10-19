class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        # Time and Space Complexity: O(N)
        prefixes = list(accumulate(nums))
        ret = []

        cur = 0
        dp = {}

        for remaining in range(3, 0, -1):
            sum, cur = self.maxSum(nums, cur, remaining, k, prefixes, dp)
            ret.append(cur)
            cur += k

        return ret

    def maxSum(self, nums, i, remaining, k, prefixes, dp):
        if (i, remaining) in dp:
            return dp[(i, remaining)]

        if remaining == 0:
            ret = 0, -1
        elif i + remaining * k > len(nums):
            ret = -1, -1
        else:
            # case 1: choose subarray from current position
            cand_sum1 = prefixes[i + k - 1]
            cand_start1 = i

            if i > 0:
                cand_sum1 -= prefixes[i - 1]

            cand_sum1 += self.maxSum(nums, i + k, remaining - 1, k, prefixes, dp)[0]

            # case 2: skip i
            cand_sum2, cand_start2 = self.maxSum(nums, i + 1, remaining, k, prefixes, dp)

            if cand_sum2 <= cand_sum1:
                ret = cand_sum1, cand_start1
            else:
                ret = cand_sum2, cand_start2

        dp[(i, remaining)] = ret
        return ret
