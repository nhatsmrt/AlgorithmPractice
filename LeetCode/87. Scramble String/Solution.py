class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        # Time Complexity: O(N^4)
        # Space Complexity: O(N^3)

        @cache
        def match(begin1, end1, begin2) -> bool:
            end2 = begin2 + end1 - begin1

            if end1 - begin1 == 0:
                return s1[begin1] == s2[begin2]

            diff = 0
            diff_cnt = Counter()
            i, j = begin1, begin2

            for first_size in range(1, end1 - begin1 + 1):
                ret = match(begin1, begin1 + first_size - 1, begin2) and match(begin1 + first_size, end1, begin2 + first_size)
                ret = ret or match(begin1, begin1 + first_size - 1, end2 - first_size + 1) and match(begin1 + first_size, end1, begin2)

                if ret:
                    break
            else:
                ret = False

            return ret

        return match(0, len(s1) - 1, 0)
