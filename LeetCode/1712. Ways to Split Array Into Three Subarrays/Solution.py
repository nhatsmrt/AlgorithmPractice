class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        # Time and Space Complexity: O(N)

        MOD = 1000000007
        prefix = list(accumulate(nums))

        first_end = 0
        start, end = 0, 1 # range of where second array ends
        ret = 0

        for first_end in range(len(nums)):
            start = max(start, first_end + 1)

            while start < len(nums) and prefix[start] < 2 * prefix[first_end]:
                start += 1

            end = max(start, end)
            while end + 1 < len(nums) and prefix[-1] - prefix[end] >= prefix[end] - prefix[first_end]:
                end += 1

            ret += end - start
            ret %= MOD

        return ret
