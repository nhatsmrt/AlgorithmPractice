class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        # Time and Space Complexity: O(N)

        # B is a rotation of A iff B is a substring of A + A

        if len(A) != len(B):
            return False

        A += A
        lps = self.lps(B)

        B_ind = 0
        A_ind = 0


        while A_ind < len(A) and B_ind < len(B):
            while B_ind > 0 and A[A_ind] != B[B_ind]:
                B_ind = lps[B_ind - 1]

            if A[A_ind] == B[B_ind]:
                B_ind += 1

            A_ind += 1


        return B_ind == len(B)


    def lps(self, s: str) -> List[int]:
        # lps[i] = length of longest prefix of s[:i + 1] that is also suffix

        ret = [0]

        for i in range(1, len(s)):
            cur = ret[i - 1]

            while cur > 0 and s[cur] != s[i]:
                cur = ret[cur - 1]

            if s[cur] == s[i]:
                ret.append(cur + 1)
            else:
                ret.append(0)

        return ret
