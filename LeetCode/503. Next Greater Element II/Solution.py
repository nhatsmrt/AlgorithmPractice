from collections import deque


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        arr_len = len(nums)
        nums += nums

        # rngv[i] = nearest greater value to the right of a[i]
        # at most len(nums) from i
        # (computable using deque)
        # Time and space complexity: O(N)

        rngv = [-1] * len(nums)
        candidates = deque()

        for i in range(len(nums) - 1, -1, -1):
            while len(candidates) > 0 and candidates[0][1] - i >= arr_len:
                candidates.popleft()

            while len(candidates) > 0 and candidates[-1][0] <= nums[i]:
                candidates.pop()

            if len(candidates) > 0:
                rngv[i] = candidates[-1][0]

            candidates.append((nums[i], i))

        return rngv[:arr_len]
