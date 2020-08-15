class Solution:
    def findPermutation(self, s: str) -> List[int]:
        ret = [1]
        self.build(s, 0, ret)
        return ret

    def build(self, s, pos, ret):
        # increase the peak:

        cnt = 0
        while pos < len(s) and s[pos] == "D":
            ret[-1] += 1
            pos += 1
            cnt += 1

        peak = ret[-1]

        for i in range(1, cnt + 1):
            ret.append(peak - i)

        if pos < len(s):
            ret.append(peak + 1)
            self.build(s, pos + 1, ret)
        
