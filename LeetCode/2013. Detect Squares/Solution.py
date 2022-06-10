class DetectSquares:

    def __init__(self):
        # Space Complexity: O(N)

        self.main_diag_index = {}
        self.anti_diag_index = {}
        self.points_cnt = Counter()

    def add(self, point: List[int]) -> None:
        # Time Complexity: O(1)

        point = tuple(point)

        main_ind = point[0] + point[1]
        anti_ind = point[0] - point[1]

        for ind, index in zip((main_ind, anti_ind), (self.main_diag_index, self.anti_diag_index)):
            if ind not in index:
                index[ind] = set()

            index[ind].add(point)

        self.points_cnt[point] += 1


    def count(self, point: List[int]) -> int:
        # Time Complexity: O(N) worst case!

        point = tuple(point)
        ret = 0


        main_ind = point[0] + point[1]
        anti_ind = point[0] - point[1]

        for ind, index in zip((main_ind, anti_ind), (self.main_diag_index, self.anti_diag_index)):
            for other_diag_pt in index.get(ind, []):
                if other_diag_pt != point:
                    fst = point[0], other_diag_pt[1]
                    thrd = other_diag_pt[0], point[1]

                    ret += self.points_cnt[other_diag_pt] * self.points_cnt[fst] * self.points_cnt[thrd]

        return ret




# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
