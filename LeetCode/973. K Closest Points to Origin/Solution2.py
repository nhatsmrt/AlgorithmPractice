class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        # Average Time and Space Complexity: O(N)

        def dist_sq(point):
            return point[0] ** 2  + point[1] ** 2

        def swap(lst, i, j):
            tmp = lst[i]
            lst[i] = lst[j]
            lst[j] = tmp

        points_with_dist = list(zip(map(dist_sq, points), range(len(points))))
        ret = []

        while len(points_with_dist) > K:
            pivot_index = int(random.random() * len(points_with_dist))
            pivot_val = points_with_dist[pivot_index]
            swap(points_with_dist, pivot_index, 0)
            left_boundary = 0

            for i in range(1, len(points_with_dist)):
                if points_with_dist[i] < pivot_val:
                    left_boundary += 1
                    swap(points_with_dist, left_boundary, i)

            swap(points_with_dist, 0, left_boundary)
            rank = left_boundary + 1


            if rank == K:
                points_with_dist = points_with_dist[:rank]
            elif K < rank:
                points_with_dist = points_with_dist[:left_boundary]
            else:
                ret.extend([points[i] for _, i in points_with_dist[:rank]])
                points_with_dist = points_with_dist[rank:]
                K -= rank


        ret.extend([points[i] for _, i in points_with_dist])
        return ret
