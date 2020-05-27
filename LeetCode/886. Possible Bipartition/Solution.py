class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        # Time and Space Complexity: O(V + E)

        adj_lists = {}

        for edge in dislikes:
            if edge[0] not in adj_lists:
                adj_lists[edge[0]] = set()

            if edge[1] not in adj_lists:
                adj_lists[edge[1]] = set()

            adj_lists[edge[0]].add(edge[1])
            adj_lists[edge[1]].add(edge[0])

        self.adj_lists = adj_lists
        self.parts = [set(), set()]

        unvisited = set(i for i in range(1, N + 1))

        while len(unvisited) > 0:
            if not self.partition(unvisited.pop(), unvisited, 0):
                return False

        return True

    def partition(self, person: int, unvisited: set, part: int):
        self.parts[part].add(person)

        for enemy in self.adj_lists.get(person, []):
            if enemy in self.parts[part]:
                return False
            elif enemy in unvisited:
                unvisited.remove(enemy)
                if not self.partition(enemy, unvisited, part ^ 1):
                    return False

        return True
