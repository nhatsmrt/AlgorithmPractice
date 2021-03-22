class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        # Time Complexity: O(sum(|word|) + sum(|query|))

        correct_match = set(wordlist)
        cap_match = {word.lower(): word for word in reversed(wordlist)}
        vowel_match = {re.sub(r"[aeiou]", "#", word.lower()): word for word in reversed(wordlist)}

        ret = []
        for query in queries:
            if query in correct_match:
                ret.append(query)
            elif query.lower() in cap_match:
                ret.append(cap_match[query.lower()])
            elif re.sub(r"[aeiou]", "#", query.lower()) in vowel_match:
                ret.append(vowel_match[re.sub(r"[aeiou]", "#", query.lower())])
            else:
                ret.append("")

        return ret
