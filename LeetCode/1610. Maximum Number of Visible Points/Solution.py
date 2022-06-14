def polar_angl(pt): # polar angle in (0, 2pi)
    return math.atan2(*reversed(pt)) + math.pi

def in_range(fst, snd, range_angle):
    # find the angle in (0, 2pi)
    a1 = polar_angl(fst)
    a2 = polar_angl(snd)

    if a1 + range_angle <= 2 * math.pi:
        return a1 <= a2 and a2 <= a1 + range_angle
    else: # wrap around
        end_angle = (a1 + range_angle) - 2 * math.pi

        return a1 <= a2 or a2 <= end_angle


class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        # Time Complexity: O(N log N)
        # Space Complexity: O(N)

        angle = angle / 180 * math.pi
        location = tuple(location)

        # recenter the points:
        points = list(map(lambda pt: (pt[0] - location[0], pt[1] - location[1]), points))

        # remove point at location:
        original_num_points = len(points)
        points = list(filter(lambda pt: pt != (0, 0), points))
        num_pt_at_ctr = original_num_points - len(points)

        # sort the points by angle:
        points.sort(key=polar_angl)

        # angular sweep:
        end = 0
        ret = 0
        num_points = len(points)
        points = points + points # duplicate the points list to handle wrap-around

        for i, anchor in enumerate(points[:num_points]):
            anchor_angl = polar_angl(anchor)

            while end + 1 < len(points) and end - i + 1 < num_points and in_range(anchor, points[end + 1], angle):
                end += 1

            ret = max(ret, end - i + 1)

        return ret + num_pt_at_ctr
