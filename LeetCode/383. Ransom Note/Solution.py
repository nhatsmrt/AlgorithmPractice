class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note_cnt = self.generate_cnt(ransomNote)
        magazine_cnt = self.generate_cnt(magazine)

        for i in range(26):
            if note_cnt[i] > magazine_cnt[i]:
                return False

        return True

    def generate_cnt(self, text: str) -> List[int]:
        ret = [0] * 26
        for char in text:
            ret[ord(char) - ord('a')] += 1

        return ret
        
