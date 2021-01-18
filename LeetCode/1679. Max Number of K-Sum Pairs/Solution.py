class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # Time and Space Complexity: O(N)
        counter = Counter(nums)

        ret = 0
        for num in counter:
            if num * 2 == k:
                ret += counter[num] // 2
            elif num < k - num:
                ret += min(counter[num], counter[k - num])

        return ret
