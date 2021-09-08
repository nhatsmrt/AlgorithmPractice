class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        # Time and Space Complexity: O(N)

        cum_shift = reversed(list(accumulate(reversed(shifts))))

        def shift_char(s: str, shift_amount: int) -> str:
            return chr((ord(s) - ord('a') + shift_amount) % 26 + ord('a'))

        return "".join(starmap(shift_char, zip(s, cum_shift)))
