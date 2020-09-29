class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        # Time and Space Complexity: O(N)

        if k < 0:
            return 0

        if not k:
            counter = collections.Counter(nums)
            return len(set(filter(lambda x: counter[x] > 1, nums)))

        nums = set(nums)

        ret = 0
        for num in nums:
            if num + k in nums:
                ret += 1

        return ret
