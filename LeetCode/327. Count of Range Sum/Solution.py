from bisect import bisect, bisect_left, bisect_right


class Node:
    def __init__(self, lower, upper):
        self.left, self.right = None, None
        self.lower, self.upper = lower, upper
        self.cnt = 0

    def __repr__(self):
        ret = ['{', str(self.cnt), ", ", str(self.lower), ", ", str(self.upper)]
        if self.left is not None:
            ret.append(", ")
            ret.append(self.left.__repr__())
            ret.append(", ")
            ret.append(self.right.__repr__())

        ret.append('}')
        return ''.join(ret)


class WeightedST:
    def __init__(self, upper_bound: int):
        self.root = Node(0, upper_bound)
        self.build(self.root)

    def build(self, node: Node):
        if node.lower < node.upper:
            mid = node.lower + (node.upper - node.lower) // 2
            node.left = Node(node.lower, mid)
            node.right = Node(mid + 1, node.upper)

            self.build(node.left)
            self.build(node.right)

    def inc(self, value: int):
        self.inc_from(self.root, value)

    def inc_from(self, node: Node, value: int):
        if node is not None and node.lower <= value and value <= node.upper:
            node.cnt += 1

            self.inc_from(node.left, value)
            self.inc_from(node.right, value)

    def count(self, lower: int, upper: int):
        return self.count_from(self.root, lower, upper)

    def count_from(self, node: Node, lower: int, upper: int):
        if node.upper < lower or node.lower > upper:
            return 0

        if node.lower >= lower and node.upper <= upper:
            return node.cnt

        return self.count_from(node.left, lower, upper) + self.count_from(node.right, lower, upper)

    def __repr__(self):
        return self.root.__repr__()




class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        # Time Complexity: O(n log n)
        # Space Complexity: O(n)

        prefixes = [0]
        for num in nums:
            prefixes.append(num + prefixes[-1])

        # Coordinate compression:
        sorted_prefixes = sorted(prefixes)
        coord_map = {}
        for i in range(len(sorted_prefixes)):
            coord_map[sorted_prefixes[i]] = i

        # O(n) for construction
        tree = WeightedST(len(prefixes) - 1)
        ret = 0

        # O(log n) per query (2 binary searches, one range query, one add query)
        # n + 1 queries, so O(n log n) in total
        for prefix in prefixes:
            upper_bound = bisect_right(sorted_prefixes, prefix - lower)
            lower_bound = bisect_left(sorted_prefixes, prefix - upper)

            if upper_bound == len(sorted_prefixes) or sorted_prefixes[upper_bound] > prefix - lower:
                upper_bound -= 1

            ret += tree.count(lower_bound, upper_bound)
            tree.inc(coord_map[prefix])

        return ret
