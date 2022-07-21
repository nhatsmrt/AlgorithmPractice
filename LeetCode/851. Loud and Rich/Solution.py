class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        # Time and Space Complexity: O(V + E)

        adj_list = {i: [] for i in range(len(quiet))}
        incoming = [0] * len(quiet)

        for rich, poor in richer:
            incoming[rich] += 1
            adj_list[poor].append(rich)

        ordering = []
        no_incoming = deque(i for i in range(len(quiet)) if incoming[i] == 0)

        while no_incoming:
            person = no_incoming.popleft()
            ordering.append(person)

            for rich in adj_list[person]:
                incoming[rich] -= 1

                if not incoming[rich]:
                    no_incoming.append(rich)

        ret = list(range(len(quiet)))
        for person in reversed(ordering):
            for rich in adj_list[person]:
                if quiet[ret[person]] > quiet[ret[rich]]:
                    ret[person] = ret[rich]

        return ret
