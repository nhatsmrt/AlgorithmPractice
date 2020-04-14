# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        low = 0
        last = high = mountain_arr.length() - 1

        # Ternary search to find Peak:
        while low < high:

            m1 = low + (high - low) // 3
            m2 = high - (high - low) // 3

            v1 = mountain_arr.get(m1)
            v2 = mountain_arr.get(m2)

            if v1 == v2:
                low = m1 + 1
                high = m2 - 1
            elif v1 < v2:
                low = m1 + 1
            else:
                high = m2 - 1

        peak = low

        ret = self.bin_search(mountain_arr, 0, peak, target)
        if ret != -1:
            return ret

        return self.bin_search(mountain_arr, peak + 1, last, target, True)

    def bin_search(self, mountain_arr: 'MountainArray', low: int, high: int, target: int, reverse: bool=False) -> int:

        while low < high:
            mid = low + (high - low) // 2
            mid_v = mountain_arr.get(mid)

            if mid_v == target:
                return mid
            elif mid_v < target:
                if reverse:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if reverse:
                    low = mid + 1
                else:
                    high = mid - 1

        if mountain_arr.get(low) == target:
            return low

        return -1
