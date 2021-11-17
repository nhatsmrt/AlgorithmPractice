class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        # Time and Space Complexity: O(|len(word)| for word in s1 + s2)

        words1 = Counter(s1.split(" "))
        words2 = Counter(s2.split(" "))

        ret = []

        for cnter in [words1, words2]:
            for word in cnter:
                if words1[word] + words2[word] == 1:
                    ret.append(word)

        return ret
