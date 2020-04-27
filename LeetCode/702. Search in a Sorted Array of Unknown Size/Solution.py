# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """

        # Time Complexity: O(log pos)
        # Space Complexity: O(1)

        low = 0
        high = 1

        while reader.get(high) < target:
            low = high + 1
            high *= 2

        while low < high:
            mid = low + (high - low) // 2
            mid_val = reader.get(mid)

            if mid_val == target:
                return mid
            elif mid_val < target:
                low = mid + 1
            else:
                high = mid - 1

        if reader.get(low) == target:
            return low
        else:
            return -1
        
