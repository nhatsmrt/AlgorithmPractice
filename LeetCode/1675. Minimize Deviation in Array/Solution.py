from sortedcontainers import SortedList


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        # Time Complexity: O(N (log W * log N))
        # Space Complexity: O(N)

        # If num is even, then its minimum possible value at the end is num divided
        # by all of its factors of 2
        # and the maximum possible value is num itself.

        # If num is odd, then its maximum possible value at the end is num * 2
        # (since each number can be multiply by 2 only once)
        # and the minimum possible value is num itself.

        # Starting from the minimum possible values of all numbers in the array
        # we can only multiply by 2

        # At each iteration, the only way to decrease the deviation is to
        # multiply by 2 the minimum number (if possible)

        # Note that there exists a sequence of multiply-min-only operations
        # such that morph the original configuration (i.e min values only)
        # to an optimal solution.


        def extract_pow_2(num: int) -> int:
            if num % 2:
                return num
            else:
                return extract_pow_2(num // 2)


        ranges = SortedList()
        for num in nums:
            if num % 2:
                ranges.add((num, num * 2))
            else:
                ranges.add((extract_pow_2(num), num))

        ret = ranges[-1][0] - ranges[0][0]
        while ranges[0][0] < ranges[0][1]:
            min_cur_val, min_max_val = ranges.pop(0)
            new_min_val = min_cur_val * 2
            ranges.add((new_min_val, min_max_val))
            ret = min(ret, ranges[-1][0] - ranges[0][0])


        return ret
