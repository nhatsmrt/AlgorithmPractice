class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        # Time and Space Complexity: O(|text|)

        words = text.split(" ")

        ret = []
        for i in range(len(words) - 2):
            if words[i] == first and words[i + 1] == second:
                ret.append(words[i + 2])

        return ret
