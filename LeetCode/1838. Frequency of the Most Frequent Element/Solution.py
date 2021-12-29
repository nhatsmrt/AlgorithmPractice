class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # Time Complexity: O(N log N)
        # Space Complexity: O(N)

        nums.sort()

        prefixes = list(accumulate(nums))
        ret = 0

        for val in set(nums):
            start, end = bisect_left(nums, val), bisect_right(nums, val)
            freq = end - start

            low = 0
            high = start

            while low < high:
                mid = low + (high - low) // 2

                num_values = start - mid
                targ = val * num_values
                existing = prefixes[start - 1] - prefixes[mid - 1] if mid else prefixes[start - 1]

                if targ - existing > k:
                    low = mid + 1
                else:
                    high = mid


            ret = max(ret, freq + start - low)

        return ret
