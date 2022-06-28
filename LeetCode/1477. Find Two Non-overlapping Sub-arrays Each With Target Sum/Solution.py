INF_LEN = 1000000000


class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        # Time and Space Complexity: O(N)

        prefixes = [0] + list(accumulate(arr))

        prefix_index_from_left = {}
        min_length_left = []


        def min_length_end_at(prefixes, target):
            ret = []
            index = {}

            for i, prefix in enumerate(prefixes):
                before = prefix - target

                if before in index:
                    ret.append(i - index[before])
                else:
                    ret.append(None)

                index[prefix] = i

            return ret

        def acc(length_arr):
            ret = []

            for length in length_arr:
                if not ret or ret[-1] is None:
                    ret.append(length)
                elif length is None:
                    ret.append(ret[-1])
                else:
                    ret.append(min(ret[-1], length))

            return ret

        left = acc(min_length_end_at(prefixes, target))
        right = acc(min_length_end_at(prefixes[::-1], -target))[::-1]

        ret = INF_LEN
        for left_min, right_min in zip(left, right):
            if left_min and right_min:
                ret = min(ret, left_min + right_min)

        if ret != INF_LEN:
            return ret

        return -1
