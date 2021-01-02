class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        # Time and Space Complexity: O(N)

        cnter = Counter(s)

        num_odd = 0

        for char in cnter:
            num_odd += cnter[char] % 2

        return num_odd <= 1
