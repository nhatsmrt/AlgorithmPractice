def dist(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def dfs(node, adj_lists, visited):
    ret = 1

    for neigh in adj_lists[node]:
        if neigh not in visited:
            visited.add(neigh)
            ret += dfs(neigh, adj_lists, visited)

    return ret

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        # Time Complexity: O(V(V + E))
        # Space Complexity: O(V + E)

        adj_lists = {i: [] for i in range(len(bombs))}

        for i in range(len(bombs)):
            for j in range(i + 1, len(bombs)):
                x1, y1, r1 = bombs[i]
                x2, y2, r2 = bombs[j]

                d = dist(x1, y1, x2, y2)

                if d <= r1:
                    adj_lists[i].append(j)

                if d <= r2:
                    adj_lists[j].append(i)

        ret = 0
        for i in range(len(bombs)):
            visited = set([i])
            ret = max(ret, dfs(i, adj_lists, visited))

        return ret
