class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False

        similar = {}

        for pair in similarPairs:
            if pair[0] not in similar:
                similar[pair[0]] = set()
            if pair[1] not in similar:
                similar[pair[1]] = set()

            similar[pair[0]].add(pair[1])
            similar[pair[1]].add(pair[0])


        for word1, word2 in zip(sentence1, sentence2):
            if word1 != word2 and word1 not in similar.get(word2, []):
                return False

        return True
