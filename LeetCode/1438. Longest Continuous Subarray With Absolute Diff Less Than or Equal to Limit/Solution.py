from sortedcontainers import SortedDict


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # Time Complexity: O(N log N) (assuming SortedDict has time complexity of BBST)

        window_multiset = SortedDict()

        start = 0
        end = start

        ret = 0

        while start < len(nums) and end < len(nums):
            if self.can_add(window_multiset, nums[end], limit):
                window_multiset[nums[end]] = window_multiset.get(nums[end], 0) + 1
                end += 1
            else:
                ret = max(end - start, ret)

                window_multiset[nums[end]] = window_multiset.get(nums[end], 0) + 1
                while not self.is_valid_window(window_multiset, limit):
                    self.remove_multiset(window_multiset, nums[start])
                    start += 1

                end += 1

        ret = max(end - start, ret)

        return ret

    def remove_multiset(self, window_multiset: SortedDict, num: int):
        window_multiset[num] -= 1

        if not window_multiset[num]:
            window_multiset.pop(num)

    def is_valid_window(self, window_multiset: SortedDict, limit: int) -> bool:
        view = window_multiset.keys()
        return view[-1] - view[0] <= limit

    def can_add(self, window_multiset: SortedDict, cand: int, limit: int) -> bool:
        if not len(window_multiset):
            return True

        view = window_multiset.keys()
        return abs(cand - view[0]) <= limit and abs(cand - view[-1]) <= limit
