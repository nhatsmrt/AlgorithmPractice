class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Time and Space Complexity: O(N)

        # Idea: find the largest window
        # such that # of characters - # of the most frequent char <= k

        # Observation: for each char added to the window
        # difference between # of char and # of the most
        # frequent char never decrease

        # This suggests we can use a two pointer approach

        def char_ind(c):
            return ord(c) - ord('A')

        if not s:
            return 0

        ret = 0
        start = 0
        end = 0

        counter = [0] * 26
        counter[char_ind(s[0])] += 1

        while start < len(s) and end < len(s):
            if end + 1 < len(s) and self.is_addable(counter, char_ind(s[end + 1]), k):
                end += 1
                counter[char_ind(s[end])] += 1
            else:
                ret = max(ret, end - start + 1)

                if end + 1 < len(s):
                    while start <= end and not self.is_addable(counter, char_ind(s[end + 1]), k):
                        counter[char_ind(s[start])] -= 1
                        start += 1


                    counter[char_ind(s[end + 1])] += 1
                end += 1

        return ret

    def is_addable(self, counter, char_ind, k):
        max_cnt = max(counter)
        sum_cnt = sum(counter)

        return counter[char_ind] == max_cnt or sum_cnt + 1 - max_cnt <= k
