class Solution:
    INTEGER_PATTERN = r"[-+]?\d+"
    DECIMAL_PATTERN = r"[-+]?(\d+\.\d*|\.\d+)"
    VALID_PATTERN = f"^({INTEGER_PATTERN}|{DECIMAL_PATTERN})([eE]{INTEGER_PATTERN})?$"
    MATCHER = re.compile(VALID_PATTERN)

    def isNumber(self, s: str) -> bool:
        # Time Complexity: O(|s|)
        # Space Complexity: O(1)
        return self.MATCHER.match(s) is not None
