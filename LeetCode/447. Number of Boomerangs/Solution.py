class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        # Time Complexity: O(N^2)
        # Space Complexity: O(N)

        dist_cnt = [Counter() for i in range(len(points))]

        ret = 0
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                fst, snd = points[i], points[j]

                dist_sq = (fst[0] - snd[0]) ** 2 + (fst[1] - snd[1]) ** 2
                ret += dist_cnt[i][dist_sq] + dist_cnt[j][dist_sq]

                dist_cnt[i][dist_sq] += 1
                dist_cnt[j][dist_sq] += 1

        return ret * 2
