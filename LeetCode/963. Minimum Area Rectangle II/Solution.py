def shoelace(points):
    fst = sum(points[i][0] * points[(i + 1) % len(points)][1] for i in range(len(points)))
    snd = sum(points[i][1] * points[(i + 1) % len(points)][0] for i in range(len(points)))

    return 0.5 * abs(fst - snd)

def midpoint(point1, point2):
    return ((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2)

def dist(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + abs(point2[1] - point1[1]) ** 2)


INF = 1000000000

class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        # Time Complexity: O(N^3)
        # Space Complexity: O(N^2)

        ret = INF
        cent_diag = {}

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                fst, snd = points[i], points[j]
                key = midpoint(fst, snd), dist(fst, snd)

                if key not in cent_diag:
                    cent_diag[key] = []

                cent_diag[key].append((i, j, fst, snd))

        for key in cent_diag:
            diags = cent_diag[key]

            for fst_diag_ind in range(len(diags)):
                for snd_diag_ind in range(fst_diag_ind + 1, len(diags)):
                    fst_diag = diags[fst_diag_ind]
                    snd_diag = diags[snd_diag_ind]
                    ret = min(ret, shoelace([fst_diag[2], snd_diag[2], fst_diag[3], snd_diag[3]]))

        if ret == INF:
            return 0

        return ret
