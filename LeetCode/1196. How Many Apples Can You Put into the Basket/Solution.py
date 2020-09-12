class Solution:
    def maxNumberOfApples(self, arr: List[int]) -> int:
        arr = list(itertools.accumulate(sorted(arr)))

        low = 0
        high = len(arr)

        while low < high:
            mid = high - (high - low) // 2

            if mid == 0:
                cand = 0
            else:
                cand = arr[mid - 1]

            if cand <= 5000:
                low = mid
            else:
                high = mid - 1

        return low
