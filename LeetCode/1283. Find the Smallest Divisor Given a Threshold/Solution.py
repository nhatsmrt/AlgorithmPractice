from functools import partial


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        # Time Complexity: O(N log MAX)

        low = 1
        high = max(nums)

        while low < high:
            mid = low + (high - low) // 2

            check = sum(map(partial(self.int_div, second = mid), nums))

            if check <= threshold:
                high = mid
            else:
                low = mid + 1

        return low

    def int_div(self, first, second):
        if first % second == 0:
            return first // second
        else:
            return first // second + 1
