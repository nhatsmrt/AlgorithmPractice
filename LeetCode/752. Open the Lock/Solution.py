from collections import deque


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == "0000":
            return 0

        deadends = set(deadends)
        touched = set()

        if target in deadends:
            return -1

        traverse = deque()
        traverse.append(("0000", 0))
        touched.add("0000")

        while len(traverse) > 0:
            comb, dist = traverse.popleft()

            if comb not in deadends:
                neighbors = self.generate_neighbors(comb)
                for neighbor in neighbors:
                    if neighbor == target:
                        return dist + 1

                    if neighbor not in touched:
                        touched.add(neighbor)
                        traverse.append((neighbor, dist + 1))

        return -1

    def generate_neighbors(self, comb: str) -> List[str]:
        ret = []
        comb_chars = [int(dig) for dig in comb]

        for i in range(4):
            comb_chars[i] = (comb_chars[i] + 1) % 10
            ret.append(''.join([str(char) for char in comb_chars]))
            comb_chars[i] = (comb_chars[i] - 1) % 10

            comb_chars[i] = (comb_chars[i] - 1) % 10
            ret.append(''.join([str(char) for char in comb_chars]))
            comb_chars[i] = (comb_chars[i] + 1) % 10

        return ret

        
