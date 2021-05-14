class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        # Time Complexity: O(N log N)
        # Space Complexity: O(N)

        lis = self.longestIncreasingSubsequence(nums)
        lds = self.longestIncreasingSubsequence(nums[::-1])[::-1]

        ret = len(nums)
        for i in range(len(nums)):
            if lis[i] * lds[i] > 0:
                ret = min(ret, len(nums) - lis[i] - lds[i] - 1)

        return ret

    def longestIncreasingSubsequence(self, nums: List[int]):
        # patience sort algorithm
        piles = []
        lis = []  # lis[i] = length of longest increasing sequence ending in nums[i]

        for num in nums:
            low = 0
            high = len(piles)

            while low < high:
                mid = (low + high) // 2

                if piles[mid][-1] >= num:
                    high = mid
                else:
                    low = mid + 1

            lis.append(low)
            if low == len(piles):
                piles.append([])

            piles[low].append(num)

        return lis 
