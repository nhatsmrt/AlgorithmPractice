class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda course: course[1])
        ret = 0
        curTotalTime = 0
        durations = []

        for course in courses:
            if course[0] + curTotalTime <= course[1]:
                ret += 1
                curTotalTime += course[0]
                heapq.heappush(durations, -course[0])
            elif len(durations) > 0 and -durations[0] >= course[0]:
                curTotalTime += course[0] + durations[0]
                heapq.heappop(durations)
                heapq.heappush(durations, -course[0])
        return ret
        
