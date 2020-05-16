class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # Time and Space Complexity: O(N + range(nums))

        low, high = min(nums), max(nums)
        buckets = [0] * (high - low + 1)
        sorted_nums = [0] * len(nums)

        for num in nums:
            buckets[num - low] += 1

        for i in range(1, len(buckets)):
            buckets[i] += buckets[i - 1]

        for i in range(len(nums) - 1, -1, -1):
            sorted_nums[buckets[nums[i] - low] - 1] = nums[i]
            buckets[nums[i] - low] -= 1

        return sum(sorted_nums[i] for i in range(len(nums)) if i % 2 == 0)
        
