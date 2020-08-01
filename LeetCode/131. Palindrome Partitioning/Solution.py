class Solution:
    def partition(self, s: str) -> List[List[str]]:
        is_palindrome = {}
        for i in range(len(s)):
            for j in range(i, len(s)):
                is_palindrome[(i, j)] = self.check_palindrome(s[i:j + 1])

        self.is_palindrome = is_palindrome
        ret = []
        self.build(s, 0, 0, [], ret)

        return ret

    def build(self, s: str, start: int, end: int, sol: List[str], ret: List[List[str]]):
        if end == len(s):
            if start == end:
                ret.append([part_str for part_str in sol])
        else:
            end += 1
            self.build(s, start, end, sol, ret)

            if self.is_palindrome[(start, end - 1)]:
                sol.append(s[start:end])
                self.build(s, end, end, sol, ret)
                sol.pop()


    def check_palindrome(self, part: str) -> bool:
        if not part:
            return True

        for i in range(len(part) // 2):
            if part[i] != part[len(part) - i - 1]:
                return False

        return True
