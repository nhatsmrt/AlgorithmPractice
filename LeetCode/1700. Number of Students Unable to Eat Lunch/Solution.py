class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # Time and Space Complexity: O(N)

        students_counter = Counter(students)

        for i, sandwich in enumerate(sandwiches):
            if students_counter[sandwich]:
                students_counter[sandwich] -= 1
            else:
                return len(students) - i

        return 0
