class Solution:
    def minJumps(self, arr: List[int]) -> int:
        # Time and Space Complexity: O(N)

        index = {}

        for i, num in enumerate(arr):
            if num not in index:
                index[num] = []

            index[num].append(i)


        traverse = deque([(0, 0)])
        visited = {0}

        while traverse:
            pos, dist = traverse.popleft()

            if pos == len(arr) - 1:
                return dist

            if pos - 1 >= 0 and pos - 1 not in visited:
                visited.add(pos - 1)
                traverse.append((pos - 1, dist + 1))

            if pos + 1 < len(arr) and pos + 1 not in visited:
                visited.add(pos + 1)
                traverse.append((pos + 1, dist + 1))

            if arr[pos] in index:
                for neigh in index[arr[pos]]:
                    if neigh not in visited:
                        visited.add(neigh)
                        traverse.append((neigh, dist + 1))


                index.pop(arr[pos])
