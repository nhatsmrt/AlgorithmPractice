class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        # Time Complexity: O(N^3)
        # Space Complexity: O(N)

        visits = sorted(list(zip(username, timestamp, website)), key=lambda visit: visit[1])

        # group visit by person:
        by_person = {}
        for visit in visits:
            if visit[0] not in by_person:
                by_person[visit[0]] = []
            by_person[visit[0]].append(visit[2])

        # count occurences of 3 sequences:
        three_seq_cnt = {}
        for person in by_person:
            person_visit = by_person[person]
            for i in range(len(person_visit) - 2):
                for j in range(i + 1, len(person_visit) - 1):
                    for k in range(j + 1, len(person_visit)):
                        code = f"{person_visit[i]} {person_visit[j]} {person_visit[k]}"
                        if code not in three_seq_cnt:
                            three_seq_cnt[code] = set()
                        three_seq_cnt[code].add(person)

        # find the occurences of 3 sequences with highest count:
        cur_max = 0
        cur_seq = ""
        for seq in three_seq_cnt:
            if len(three_seq_cnt[seq]) > cur_max or \
            (len(three_seq_cnt[seq]) == cur_max and seq < cur_seq):
                cur_max = len(three_seq_cnt[seq])
                cur_seq = seq

        return cur_seq.split(" ")
