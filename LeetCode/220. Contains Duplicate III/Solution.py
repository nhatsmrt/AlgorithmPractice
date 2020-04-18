class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        # Time and Space Complexity: O(n)
        # Space Complexity: O(k)

        if k <= 0 or t < 0:
            return False

        min_val = min(nums)
        for i in range(len(nums)):
            nums[i] -= min_val
        buckets = {}
        # Note that each bucket contains at most one element
        # at any time

        for i in range(len(nums)):
            ind = nums[i] // (t + 1)

            if ind in buckets:
                return True

            if ind - 1 in buckets and abs(nums[i] - buckets[ind - 1]) <= t:
                return True

            if ind + 1 in buckets and abs(nums[i] - buckets[ind + 1]) <= t:
                return True

            buckets[ind] = nums[i]
            if i >= k:
                buckets.pop(nums[i - k] // (t + 1))

        return False
            
