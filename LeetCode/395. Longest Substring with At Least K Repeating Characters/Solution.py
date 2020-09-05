def get_ind(char) -> int:
    return ord(char) - ord('a')

def get_char(ind) -> str:
    return chr(ind + ord('a'))

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        # Time and Space Complexity: O(N) (worst case, since there is at most 26 levels, and total number of work per level is O(N))

        cum_freq = [[0 for _ in range(26)] for i in range(len(s) + 1)]
        for i in range(1, len(s) + 1):
            cum_freq[i] = copy.deepcopy(cum_freq[i - 1])
            cum_freq[i][get_ind(s[i - 1])] += 1

        self.cum_freq = cum_freq
        return self.findLongest(s, 0, len(s) - 1, k)

    def findLongest(self, s, start, end, k):
        if start > end:
            return 0

        freq_substr = self.freq_substr(start, end)
        min_freq, argmin = self.find_min(freq_substr)

        if min_freq >= k:
            return end - start + 1

        char = get_char(argmin)
        ret = 0

        window_start = start
        window_end = window_start

        while window_start <= end:
            if s[window_start] == char:
                window_start += 1
                window_end = window_start
            elif window_end + 1 <= end and s[window_end + 1] != char:
                window_end += 1
            else:
                # window_start to window_end
                ret = max(ret, self.findLongest(s, window_start, window_end, k))

                window_start = window_end + 1
                window_end = window_start

        return ret

    def freq_substr(self, start, end):
        return [self.cum_freq[end + 1][i] - self.cum_freq[start][i] for i in range(26)]

    def find_min(self, freq_substr):
        min_freq, argmin = 1000000000, -1

        for i in range(26):
            if min_freq > freq_substr[i] and freq_substr[i] != 0:
                min_freq = freq_substr[i]
                argmin = i

        return min_freq, argmin
