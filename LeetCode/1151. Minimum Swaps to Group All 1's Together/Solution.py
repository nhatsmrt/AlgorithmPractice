class Solution:
    def minSwaps(self, data: List[int]) -> int:
        # Time Complexity: O(N)
        # Space Complexity: O(1)

        # Let C be number of ones in data
        # min number of swaps = C - C'
        # where C' is the number of ones in the window of size C
        # with most ones.

        num_ones = sum(data)
        cur_cnt = sum(data[:num_ones])
        ret = num_ones - cur_cnt  # first window

        for i in range(num_ones, len(data)):
            cur_cnt += data[i]
            cur_cnt -= data[i - num_ones]
            ret = min(ret, num_ones - cur_cnt)

        return ret
