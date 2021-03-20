class Solution:
    def minDeletions(self, s: str) -> int:
        # Time Complexity: O(n log n)
        # Space Complexity: O(n)

        # Greedy strategy: consider characters by descending order of frequency
        # (proof: cut-and-paste)

        cnter = Counter(iter(s))
        freqs = [(char, cnter[char]) for char in cnter]
        freqs.sort(key=lambda pair: -pair[-1])

        cur_max = 100000000000
        max_len = 0
        for char, freq in freqs:
            freq = max(0, min(freq, cur_max - 1))
            cur_max = freq
            max_len += freq

        return len(s) - max_len
