class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        # Time Complexity: O(TN^2)
        # Space Complexity: O(TN)
        clips.sort(key=lambda t:t[0])
        clips = self.simplify(clips)
        self.dp = [[None for j in range(T)] for i in range(len(clips))] # len(clips) x T
        return self.stitchDP(clips, 0, 0)

    def simplify(self, clips: List[List[int]]) -> List[List[int]]:
        ret = []
        i = 0
        j = 1

        while i < len(clips):
            j = i + 1
            endpoint = clips[i][1]

            while j < len(clips) and clips[j][0] == clips[i][0]:
                endpoint = max(endpoint, clips[j][1])
                j += 1

            ret.append([clips[i][0], endpoint])
            i = j

        return ret

    def stitchDP(self, clips: List[List[int]], t: int, i: int):
        if t >= len(self.dp[0]):
            return 0

        if i == len(self.dp):
            return -1

        if self.dp[i][t] is not None:
            return self.dp[i][t]

        ret = -1
        for j in range(i, len(clips)):
            if clips[j][0] <= t:
                candidate = self.stitchDP(clips, clips[j][1], j + 1)
                if candidate != -1 and (ret == -1 or ret > candidate + 1):
                    ret = candidate + 1

        self.dp[i][t] = ret
        return ret
