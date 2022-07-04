class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # Time and Space Complexity: O(V + E)
        # V = O(N), E = O(N^2)

        if source == target:
            return 0

        stops = list(map(set, routes))
        route_through = {}

        for route, route_stops in enumerate(routes):
            for i, stop in enumerate(route_stops):
                if stop not in route_through:
                    route_through[stop] = []

                route_through[stop].append(route)

        adj_lists = {}
        for stop in route_through:
            routes = route_through[stop]

            for r1, r2 in combinations(routes, 2):
                if r1 not in adj_lists:
                    adj_lists[r1] = []

                adj_lists[r1].append(r2)

                if r2 not in adj_lists:
                    adj_lists[r2] = []

                adj_lists[r2].append(r1)

        to_traverse = deque()
        visited = set()

        for route in route_through.get(source, []):
            to_traverse.append((1, route))
            visited.add(route)

        while to_traverse:
            dist, route = to_traverse.popleft()

            if target in stops[route]:
                return dist

            for adj_route in adj_lists.get(route, []):
                if adj_route not in visited:
                    visited.add(adj_route)
                    to_traverse.append((dist + 1, adj_route))

        return -1
