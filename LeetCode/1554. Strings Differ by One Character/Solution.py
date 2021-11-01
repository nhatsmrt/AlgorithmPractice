class Solution:
    def differByOne(self, dict: List[str]) -> bool:
        # Time Complexity: O(L^2 N)
        # Space Complexity: O(L^3 N)

        patterns = {}

        for string in dict:
            for i in range(len(string)):
                pattern = string[:i] + "*" + string[i + 1:]

                if pattern in patterns:
                    return True

                patterns[pattern] = set([string])

        return False
