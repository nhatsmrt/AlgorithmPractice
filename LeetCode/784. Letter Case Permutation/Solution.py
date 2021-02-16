class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        # Time and Space Complexity: O(N 2^N)

        def is_digit(char):
            return char in "0123456789"

        S_iter = iter(S)
        S_both_cases = map(lambda char: [char] if is_digit(char) else [char.lower(), char.upper()], S_iter)
        all_cases = product(*S_both_cases)

        return list(map(lambda comps: "".join(comps), all_cases))
