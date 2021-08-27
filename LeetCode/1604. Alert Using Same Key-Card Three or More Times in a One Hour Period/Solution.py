class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        # Time Complexity: O(N log N)
        # Space Complexity: O(N)

        def hour_to_min(hour):
            components = hour.split(":")
            return int(components[0]) * 60 + int(components[1])

        data = sorted(zip(keyName, map(hour_to_min, keyTime)))
        used = {}
        ret = set()

        for i, (name, time) in enumerate(data):
            if name not in used:
                used[name] = deque()

            while used[name] and time - used[name][0] > 60:
                used[name].popleft()

            used[name].append(time)

            if len(used[name]) >= 3:
                ret.add(name)

        return sorted(list(ret))
