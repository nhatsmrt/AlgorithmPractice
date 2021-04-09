class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        # Time and Space Complexity: O(length * N)

        prefix_counters = []
        prefix_counters.append([0] * 26)
        prefix_counters[-1][ord(s[0]) - ord('a')] += 1

        for i in range(1, len(s)):
            prefix_counters.append(copy.deepcopy(prefix_counters[-1]))
            prefix_counters[-1][ord(s[i]) - ord('a')] += 1

        def num_chars(prefix_counters, start, end):
            if start == 0:
                return len(list(filter(lambda cnt: cnt > 0, prefix_counters[end])))

            ret = 0
            for i in range(26):
                if prefix_counters[end][i] > prefix_counters[start - 1][i]:
                    ret += 1

            return ret

        substr_cnter = Counter()

        for start in range(len(s)):
            for length in range(minSize, maxSize + 1):
                if start + length <= len(s) and num_chars(prefix_counters, start, start + length - 1) <= maxLetters:
                    substr_cnter[s[start:start + length]] += 1
                else:
                    break

        if not substr_cnter:
            return 0
        return max([(substr_cnter[substr], substr) for substr in substr_cnter])[0]
