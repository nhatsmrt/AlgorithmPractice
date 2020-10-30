class STNode:
    def __init__(self, start, end):
        self.start, self.end = start, end
        self.mid = start + (end - start) // 2
        self.value = (0, 1)
        self.left, self.right = None, None # lazy


def insert(node, key, value):
    if node.start == node.end:
        node.value = merge(node.value, value)
    else:
        if not node.left:
            node.left = STNode(node.start, node.mid)
            node.right = STNode(node.mid + 1, node.end)

        if key <= node.mid:
            insert(node.left, key, value)
        else:
            insert(node.right, key, value)

        node.value = merge(node.left.value, node.right.value)


def query(node, key):
    if node.start > key:
        # range and key does not intersect
        return (0, 1)

    if node.end <= key:
        # range of node lies within range of query
        return node.value

    # intersection

    # create left and right node
    if not node.left:
        node.left = STNode(node.start, node.mid)
        node.right = STNode(node.mid + 1, node.end)

    return merge(query(node.left, key), query(node.right, key))


def merge(value_1, value_2):
    # merge two node values:
    if value_1[0] == value_2[0]:
        if value_1[0] == 0:
            return (0, 1)
        return (value_1[0], value_1[1] + value_2[1])

    return max(value_1, value_2)


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # Time Complexity: O(N log N)
        # Space Complexity: O(N)

        if not nums:
            return 0

        # coordinate compression:
        coords = {}
        for i, num in enumerate(sorted(nums)):
            coords[num] = i


        root = STNode(0, len(nums) - 1)

        # STNode(start, end) will store
        # (length of LIS, number of LIS) in the range of the node.
        # STNode(start, start) will store the (length of LIS, number of LIS)
        # whose end = start, that lies in the prefix processed so far.

        for num in nums:
            # get number of LIS so far in the range (0, num - 1)
            length_LIS, num_LIS = query(root, coords[num] - 1)

            # insert the new value:
            insert(root, coords[num], (length_LIS + 1, num_LIS))

        # return number of LIS in entire range:
        return query(root, len(nums) - 1)[1]
