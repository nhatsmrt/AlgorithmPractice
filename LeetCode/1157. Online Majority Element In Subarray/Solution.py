# Time Complexity: <O(n), O(log(n))>
# Space Complexity: O(n)
import bisect


class Node:
    def __init__(self, lower, upper):
        self.lower, self.upper = lower, upper
        self.left, self.right = None, None



class MajorityChecker:
    def __init__(self, arr: List[int]):
        self.inverted_indices = {}
        self.root = self.build(arr, 0, len(arr) - 1)

    def build(self, arr: List[int], lower: int, upper: int):
        ret = Node(lower, upper)

        if lower == upper:
            ret.maj = arr[lower]
            if arr[lower] not in self.inverted_indices:
                self.inverted_indices[arr[lower]] = []
            self.inverted_indices[arr[lower]].append(lower)
            ret.maj_score = 1
            # maj is the majority element candidate (if there is one)
            # and maj score > 0 if maj is actually the majority
            # (Similar to Boyer-Moore's algorithm)
        else:
            mid = lower + (upper - lower) // 2
            ret.left = self.build(arr, lower, mid)
            ret.right = self.build(arr, mid + 1, upper)

            if ret.left.maj == ret.right.maj:
                ret.maj = ret.left.maj
                ret.maj_score = ret.left.maj_score + ret.right.maj_score
            elif ret.left.maj_score > ret.right.maj_score:
                ret.maj = ret.left.maj
                ret.maj_score = ret.left.maj_score - ret.right.maj_score
            else:
                ret.maj = ret.right.maj
                ret.maj_score = ret.right.maj_score - ret.left.maj_score
        return ret


    def query(self, left: int, right: int, threshold: int) -> int:
        maj, maj_sc = self.get_maj(self.root, left, right)
        if maj is not None and maj_sc > 0:
            first = bisect.bisect_left(self.inverted_indices[maj], left)
            last = bisect.bisect_right(self.inverted_indices[maj], right)

            if last - first >= threshold:
                return maj
        return -1


    def get_maj(self, node: Node, lower: int, upper: int) -> int:
        # Observation: if a number is majority in A union B, and if it's not the majority in A then it's majority in B
        # (A, B are multisets)
        if node.lower > upper or node.upper < lower:
            return None, None

        if lower <= node.lower and node.upper <= upper:
            return node.maj, node.maj_score

        left_maj, left_sc = self.get_maj(node.left, lower, upper)
        right_maj, right_sc = self.get_maj(node.right, lower, upper)

        if left_maj is None:
            return right_maj, right_sc

        if right_maj is None:
            return left_maj, left_sc

        if left_maj == right_maj:
            return left_maj, left_sc + right_sc
        elif left_sc > right_sc:
            return left_maj, left_sc - right_sc
        else:
            return right_maj, right_sc - left_sc



# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)
