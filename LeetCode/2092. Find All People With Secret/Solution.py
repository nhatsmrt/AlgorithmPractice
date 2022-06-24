class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        # Time Complexity: O(V + E log E)
        # Space Complexity: O(V + E)

        meetings.sort(key=lambda m: m[-1])

        # Condense meetings list:
        meeting_sets = []
        start = 0
        end = 0

        meeting_set = {
            meetings[start][0]: {tuple(meetings[start][:2])},
            meetings[start][1]: {tuple(meetings[start][:2])}
        }
        while start < len(meetings):
            if end + 1 < len(meetings) and meetings[start][-1] == meetings[end + 1][-1]:
                end += 1

                if meetings[end][0] not in meeting_set:
                    meeting_set[meetings[end][0]] = set()

                if meetings[end][1] not in meeting_set:
                    meeting_set[meetings[end][1]] = set()

                meeting_set[meetings[end][0]].add(tuple(meetings[end][:2]))
                meeting_set[meetings[end][1]].add(tuple(meetings[end][:2]))
            else:
                meeting_sets.append(meeting_set)
                start = end + 1
                end += 1

                meeting_set = set()
                if start < len(meetings):
                    meeting_set = {
                        meetings[start][0]: {tuple(meetings[start][:2])},
                        meetings[start][1]: {tuple(meetings[start][:2])}
                    }


        ret = set([0, firstPerson])
        for meeting_set in meeting_sets:
            to_process = [per for per in meeting_set if per in ret]
            in_to_process = set(to_process)

            while to_process:
                per = to_process.pop()

                for edge in meeting_set.get(per, set()):
                    other = edge[0] + edge[1] - per

                    if other not in in_to_process:
                        to_process.append(other)
                        in_to_process.add(other)
                        ret.add(other)


        return list(ret)
    
