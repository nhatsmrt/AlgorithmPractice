class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # Time Complexity: O(sum(|word|))
        # Space Complexity: O(1)

        allowed_set = set(iter(allowed)) # size at most 26
        return sum(map(partial(self.is_str_allow, allowed=allowed_set), words))

    def is_str_allow(self, string, allowed):
        return all(map(lambda c: c in allowed, string))
