# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def build_edges(edges, node: TreeNode):
    if not node: return

    if node.val not in edges:
        edges[node.val] = {}

    for direction, child in zip(['L', 'R'], [node.left, node.right]):
        if child:
            if child.val not in edges:
                edges[child.val] = {}

            edges[node.val][child.val] = direction
            edges[child.val][node.val] = 'U'

            build_edges(edges, child)

class Stack: pass # immutable stack
class Bottom(Stack): pass
class Entry(Stack):
    def __init__(self, value: str, rest: Stack):
        self.value, self.rest = value, rest

def reconstruct(stack: Stack):
    ret = []
    cur = stack

    while not isinstance(cur, Bottom):
        ret.append(cur.value)
        cur = cur.rest

    return "".join(ret[::-1])

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # Time and Space Complexity: O(N)

        edges = {}
        build_edges(edges, root)

        # performing a bfs from startValue
        visited = set()
        traverse = deque()

        visited.add(startValue)
        traverse.append((startValue, Bottom()))

        while traverse:
            node_id, path = traverse.popleft()

            if node_id == destValue:
                return reconstruct(path)

            for neighbor in edges.get(node_id, []):
                if neighbor not in visited:
                    new_path = Entry(edges[node_id][neighbor], path)
                    visited.add(neighbor)
                    traverse.append((neighbor, new_path))
        
