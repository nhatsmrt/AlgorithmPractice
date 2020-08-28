def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def midpoint(p1, p2):
    return [(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2]

def vec(p1, p2):
    return [p1[0] - p2[0], p1[1] - p2[1]]

def dot(p1, p2):
    return p1[0] * p2[0] + p1[1] * p2[1]

def is_orth(p1, p2, p3, p4):
    return dot(vec(p1, p2), vec(p3, p4)) == 0


class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        # Time and Space Complexity: O(1)

        candidates = [(p1, p2, p3, p4), (p1, p3, p2, p4), (p1, p4, p2, p3)]
        return any(itertools.starmap(self.check_diag, candidates))

    def check_diag(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        return dist(p1, p2) and dist(p1, p2) == dist(p3, p4) and is_orth(p1, p2, p3, p4) and midpoint(p1, p2) == midpoint(p3, p4)
