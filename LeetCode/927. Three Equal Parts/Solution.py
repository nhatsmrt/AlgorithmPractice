class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        # Time and Space Complexity: O(N)

        # Idea: each part will have equal number of ones
        # Find the true value of each part by looking at the suffix part first
        # Then using this, find the prefix part (after trimming the zeros)
        # and finally, verify that the middle part is equal to the other two parts

        num_ones = list(itertools.accumulate(arr))


        total_num_ones = num_ones[-1]

        if total_num_ones % 3:
            return [-1, -1]

        if not total_num_ones:
            return [0, 2]


        suffix_start = bisect.bisect(num_ones, total_num_ones // 3 * 2)
        nonzero_len = len(arr) - suffix_start

        i = 0
        while i < len(arr) and arr[i] == 0:
            i += 1


        if (i + nonzero_len - 1) + 1 >= suffix_start or arr[i:i + nonzero_len] != arr[suffix_start:]:
            return [-1, -1]

        i += nonzero_len - 1

        midfix_end = i + 1 # eventually, j - 1
        while midfix_end < len(arr) and arr[midfix_end] == 0:
            midfix_end += 1

        if (midfix_end + nonzero_len - 1) >= suffix_start or arr[midfix_end:midfix_end + nonzero_len] != arr[suffix_start:]:
            return [-1, -1]

        j = midfix_end + nonzero_len
        
        return [i, j]
