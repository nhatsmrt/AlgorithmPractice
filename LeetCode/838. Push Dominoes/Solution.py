class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        # Time and Space Complexity: O(N)
        INF = 1000000000

        from_right = [INF] * len(dominoes)
        from_left = [INF] * len(dominoes)

        for i in range(1, len(dominoes)):
            if dominoes[i - 1] == "R":
                from_left[i] = 1
            elif dominoes[i - 1] == "." and from_left[i - 1] < INF:
                from_left[i] = from_left[i - 1] + 1

        for i in range(len(dominoes) - 2, -1, -1):
            if dominoes[i + 1] == "L":
                from_right[i] = 1
            elif dominoes[i + 1] == "." and from_right[i + 1] < INF:
                from_right[i] = from_right[i + 1] + 1


        ret = []
        for i in range(len(dominoes)):
            if dominoes[i] != "." or from_left[i] == from_right[i]:
                ret.append(dominoes[i])
            elif from_left[i] < from_right[i]:
                ret.append("R")
            else:
                ret.append("L")
        return "".join(ret)
