class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        # Time Complexity: O(N log N)
        # Space Complexity: O(1)
        clips.sort(key=lambda t:t[0])
        clips = self.simplify(clips)

        t = 0
        ret = 0
        i = 0
        j = 0

        while i < len(clips) and t < T:
            if clips[i][0] > t:
                return -1

            j = i
            best_ind = i
            furthest = clips[i][1]

            while j < len(clips) and clips[j][0] <= t:
                if furthest < clips[j][1]:
                    best_ind = j
                    furthest = clips[j][1]
                j += 1

            t = furthest
            i = j
            ret += 1

        if t >= T:
            return ret
        return -1

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
