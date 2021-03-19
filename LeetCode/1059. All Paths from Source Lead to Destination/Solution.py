class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Time and Space Complexity: O(V + E)

        adj_list = {i: set() for i in range(n)}


        for edge in edges:
            adj_list[edge[0]].add(edge[1])

        self.times = {}
        self.timestamp = 0
        self.adj_list = adj_list

        self.assign_time(source, set())
        if destination not in self.times:
            return False

        return self.verify(source, destination, set())

    def assign_time(self, node, visited):
        visited.add(node)
        start = self.timestamp
        self.timestamp += 1

        for neighbor in self.adj_list[node]:
            if neighbor not in visited:
                self.assign_time(neighbor, visited)

        end = self.timestamp
        self.times[node] = (start, end)
        self.timestamp += 1


    def verify(self, node, target, visited):
        if not self.adj_list[node]:
            return node == target

        visited.add(node)
        ret = True

        for neighbor in self.adj_list[node]:
            if neighbor in visited:
                if self.times[neighbor][0] <= self.times[node][0] and self.times[node][1] <= self.times[neighbor][1]:
                    return False
            else:
                ret = ret and self.verify(neighbor, target, visited)

        return ret
