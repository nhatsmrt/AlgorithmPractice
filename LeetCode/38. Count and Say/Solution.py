class Solution:
    def countAndSay(self, n: int) -> str:
        cur = "1"
        for i in range(n - 1):
            cur = self.nextCountAndSay(cur)

        return cur

    def nextCountAndSay(self, num: str) -> str:
        ret = []

        start = 0
        while start < len(num):
            end = start

            while end < len(num) and num[start] == num[end]:
                end += 1

            ret.append(str(end - start))
            ret.append(num[start])
            start = end

        return "".join(ret)
